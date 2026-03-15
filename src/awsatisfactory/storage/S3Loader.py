import boto3
from datetime import datetime

from awsatisfactory.config.config import BUCKET
from awsatisfactory.storage.utils import detect_content_type

class S3Loader:

    # Constructor

    def __init__(self, bucket : str = BUCKET) -> None:
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

    def upload(self, body : bytes, key : str) -> str:

        params : dict = {
            "Bucket" : self.get_bucket(),
            "Key" : key,
            "Body" : body
        }

        content_type, encoding = detect_content_type(key)
        if content_type:
            params["ContentType"] = content_type
        if encoding:
            params["ContentEncoding"] = encoding

        self.s3.put_object(**params)

        return {
            "Bucket" : self.get_bucket(),
            "Key" : key
        }