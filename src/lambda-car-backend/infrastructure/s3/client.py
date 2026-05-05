import boto3
from .config import load_s3_config


def create_s3_client():
    config = load_s3_config()
    return boto3.client("s3", region_name=config.region_name)