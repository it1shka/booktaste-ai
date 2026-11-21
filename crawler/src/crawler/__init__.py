from crawler.integrations import get_s3_client
from crawler.setup import datasets_setup


def main() -> None:
    s3 = get_s3_client()
    datasets_setup(s3)
