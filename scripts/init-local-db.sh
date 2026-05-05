#!/bin/bash
set -e

ENDPOINT_URL="http://localhost:8001"
REGION="eu-west-1"

export AWS_ACCESS_KEY_ID=fake
export AWS_SECRET_ACCESS_KEY=fake
export AWS_DEFAULT_REGION=$REGION

ADMIN_ID="11111111-1111-1111-1111-111111111111"
ADMIN_EMAIL="admin@test.com"
ADMIN_HASH='$argon2id$v=19$m=65536,t=3,p=4$r6WdjH6rFR/wl38nBO5Blg$+OJHw767tnYiXqD86x5rCPT5EGDCRUsJgLAzRrU/BjM'


create_table_if_not_exists() {
  TABLE_NAME=$1
  shift

  if aws dynamodb describe-table \
    --table-name "$TABLE_NAME" \
    --endpoint-url "$ENDPOINT_URL" >/dev/null 2>&1; then
    echo "[SKIP] Table $TABLE_NAME already exists"
  else
    echo "[CREATE] Table $TABLE_NAME"
    aws dynamodb create-table "$@" --endpoint-url "$ENDPOINT_URL"
  fi
}


create_table_if_not_exists users \
  --table-name users \
  --attribute-definitions \
      AttributeName=id,AttributeType=S \
      AttributeName=email,AttributeType=S \
  --key-schema \
      AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --global-secondary-indexes '[
    {
      "IndexName": "email-index",
      "KeySchema": [
        {"AttributeName": "email", "KeyType": "HASH"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    }
  ]'


create_table_if_not_exists cars \
  --table-name cars \
  --attribute-definitions \
      AttributeName=id,AttributeType=S \
      AttributeName=plate,AttributeType=S \
  --key-schema \
      AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --global-secondary-indexes '[
    {
      "IndexName": "plate-index",
      "KeySchema": [
        {"AttributeName": "plate", "KeyType": "HASH"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    }
  ]'


create_table_if_not_exists trips \
  --table-name trips \
  --attribute-definitions \
      AttributeName=id,AttributeType=S \
      AttributeName=user_id,AttributeType=S \
      AttributeName=car_id,AttributeType=S \
      AttributeName=status,AttributeType=S \
  --key-schema \
      AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --global-secondary-indexes '[
    {
      "IndexName": "user_id-index",
      "KeySchema": [
        {"AttributeName": "user_id", "KeyType": "HASH"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    },
    {
      "IndexName": "car_id-index",
      "KeySchema": [
        {"AttributeName": "car_id", "KeyType": "HASH"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    },
    {
      "IndexName": "car_id-status-index",
      "KeySchema": [
        {"AttributeName": "car_id", "KeyType": "HASH"},
        {"AttributeName": "status", "KeyType": "RANGE"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    }
  ]'


create_table_if_not_exists refuelings \
  --table-name refuelings \
  --attribute-definitions \
      AttributeName=id,AttributeType=S \
      AttributeName=car_id,AttributeType=S \
  --key-schema \
      AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --global-secondary-indexes '[
    {
      "IndexName": "car_id-index",
      "KeySchema": [
        {"AttributeName": "car_id", "KeyType": "HASH"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    }
  ]'


create_table_if_not_exists commits \
  --table-name commits \
  --attribute-definitions \
      AttributeName=id,AttributeType=S \
      AttributeName=code,AttributeType=S \
  --key-schema \
      AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --global-secondary-indexes '[
    {
      "IndexName": "code-index",
      "KeySchema": [
        {"AttributeName": "code", "KeyType": "HASH"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    }
  ]'


echo "[UPSERT] Admin user"

aws dynamodb put-item \
  --table-name users \
  --item "{
    \"id\": {\"S\": \"$ADMIN_ID\"},
    \"name\": {\"S\": \"admin\"},
    \"email\": {\"S\": \"$ADMIN_EMAIL\"},
    \"hashed_password\": {\"S\": \"$ADMIN_HASH\"},
    \"role\": {\"S\": \"ADMIN\"}
  }" \
  --endpoint-url "$ENDPOINT_URL"

echo "[DONE] Local DynamoDB initialized"
