import io
import boto3
from pandas import DataFrame


class CuratedLoader:

    # Constants

    BUCKET : str = "satisfactory-energy-data-lake"
    FOLDER : str = "curated"

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

    def upload(self, df : DataFrame) -> None:

        buffer : io.BytesIO = io.BytesIO()

        df.to_parquet(buffer, index=False)

        key : str = "curated/energy_charts/price/price_table.parquet"

        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=buffer.getvalue()
        )