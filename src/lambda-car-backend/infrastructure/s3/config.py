from dataclasses import dataclass
import os

@dataclass(frozen=True)

class S3Config:
    bucket_name: str
    region_name: str
    receipts_prefix: str
    endpoint_url: str = None

def load_s3_config() -> S3Config:
    return S3Config(
        bucket_name=os.getenv("S3_BUCKET_NAME", "lambda-car-receipts"),
        region_name=os.getenv("S3_REGION_NAME", "us-east-1"),
        receipts_prefix=os.getenv("S3_RECEIPTS_PREFIX", "receipts/"),
        endpoint_url=os.getenv("S3_ENDPOINT_URL")
    )