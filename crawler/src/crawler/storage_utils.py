"""Utilities based on boto3 to work with S3-compatible storage."""

from botocore.exceptions import ClientError


def ensure_bucket_exists(s3, bucket_name: str) -> None:
    """Creates a bucket with a given name if it does not exist."""
    try:
        s3.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        if e.response["Error"]["Code"] != "404":
            raise
        s3.create_bucket(Bucket=bucket_name)


def object_exists(s3, bucket_name: str, object_name: str) -> bool:
    """Checks whether an object exists."""
    try:
        s3.head_object(Bucket=bucket_name, Key=object_name)
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] != "404":
            raise
        return False
