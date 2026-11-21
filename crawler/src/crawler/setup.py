"""Module responsible for setting up environment for crawler."""

import urllib.request
from crawler.storage_utils import ensure_bucket_exists, object_exists


BOOK_RATINGS_URL = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/refs/heads/master/books.csv"
BOOK_RATINGS_BUCKET = "ratings"
BOOK_RATINGS_RAW_OBJECT = "raw.csv"


def datasets_setup(s3) -> None:
    """
    Downloads the initial book rating datasets if they're not present
    and transforms them if necessary.
    """
    ensure_bucket_exists(s3, BOOK_RATINGS_BUCKET)
    if not object_exists(s3, BOOK_RATINGS_BUCKET, BOOK_RATINGS_RAW_OBJECT):
        with urllib.request.urlopen(BOOK_RATINGS_URL) as response:
            book_ratings_raw_data = response.read()
            s3.put_object(
                Bucket=BOOK_RATINGS_BUCKET,
                Key=BOOK_RATINGS_RAW_OBJECT,
                Body=book_ratings_raw_data,
            )
