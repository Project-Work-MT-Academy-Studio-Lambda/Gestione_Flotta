import boto3
from .config import load_s3_config


def create_s3_client():
    config = load_s3_config()
    kwargs = {
        "service_name": "s3",
        "region_name": config.region_name,
    }
    if config.endpoint_url:
        kwargs["endpoint_url"] = config.endpoint_url
    return boto3.client(**kwargs)