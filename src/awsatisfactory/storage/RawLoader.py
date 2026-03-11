import json
import gzip
import boto3
from datetime import datetime

class RawLoader:

    # Constructor

    def __init__(self, bucket : str) -> None:
        self.bucket : str = bucket
        self.s3 : boto3.client = boto3.client("s3")

    # Getters and setters

    def get_bucket(self) -> str:
        return self.bucket
    
    def set_bucket(self, value: str):
        self.bucket : str = value

    def get_s3(self) -> boto3.client:
        return self.s3

    def set_s3(self, value: boto3.client):
        self.s3 : boto3.client = value

    # Methods

    def upload(self, records: list[dict], destination: str, dataset: str) -> str:

        now : datetime = datetime.now()

        key = (
            f"raw/{destination}/{dataset}/"
            f"year={now.year}/"
            f"month={now.month:02}/"
            f"day={now.day:02}/"
            f"data_{now.strftime('%Y%m%dT%H%M%S')}.json.gz"
        )

        json_lines = "\n".join(json.dumps(r) for r in records)

        # compression gzip
        compressed_data = gzip.compress(json_lines.encode("utf-8"))


        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=compressed_data,
            ContentType="application/json",
            ContentEncoding="gzip"
        )

        return key