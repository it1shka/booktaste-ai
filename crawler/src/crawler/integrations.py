"""Module responsible for integration with 3rd-party services."""

import os

import boto3
from botocore.client import Config


def get_s3_client():
    """
    Returns connection to S3-compatible storage,
    reading configuration from the env variables.
    In our case, the storage is RustFS:
    [Guide on RustFS + boto3](https://rustfs.org/developer/sdk/python.html#_3-connecting-to-rustfs).

    Expected env variables:
    - S3_ENDPOINT_URL
    - S3_ACCESS_KEY
    - S3_SECRET_KEY
    """
    s3_endpoint_url = os.getenv("S3_ENDPOINT_URL")
    assert (
        s3_endpoint_url is not None and len(s3_endpoint_url) > 0
    ), "specify S3_ENDPOINT_URL as env var"
    s3_access_key = os.getenv("S3_ACCESS_KEY")
    assert (
        s3_access_key is not None and len(s3_access_key) > 0
    ), "specify S3_ACCESS_KEY as env var"
    s3_secret_key = os.getenv("S3_SECRET_KEY")
    assert (
        s3_secret_key is not None and len(s3_secret_key) > 0
    ), "specify S3_SECRET_KEY as env var"
    return boto3.client(
        "s3",
        endpoint_url=s3_endpoint_url,
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )
