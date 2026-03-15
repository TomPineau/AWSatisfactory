import json
import gzip
import boto3
import os
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
from io import BytesIO

from awsatisfactory.storage.S3Loader import S3Loader
from awsatisfactory.config.config import BUCKET_SUB


def lambda_handler(event, context) -> dict :

    input : dict = event["output"]
    bucket : str = input["Bucket"]
    key : str = input["Key"]

    s3_loader : S3Loader = S3Loader()
    s3 : boto3.client = s3_loader.get_s3()
    response : dict = s3.get_object(
        Bucket = bucket,
        Key = key
    )
    s3_loader.set_bucket(bucket)

    compressed_file : bytes = response["Body"].read()
    rows : list = []

    with gzip.GzipFile(fileobj = BytesIO(compressed_file)) as f:
        for line in f :
            row = json.loads(line)

            row["unix_seconds"] = int(row["unix_seconds"])
            row["price"] = float(row["price"])
            row["datetime"] = datetime.fromtimestamp(row["unix_seconds"])

            rows.append(row)

    schema = pa.schema([
        ("unix_seconds", pa.int64()),
        ("price", pa.float64()),
        ("datetime", pa.timestamp("ms"))
    ])

    table = pa.Table.from_pylist(rows, schema = schema)
    buffer : BytesIO = BytesIO()
    pq.write_table(
        table,
        buffer,
        compression = "snappy"
    )

    curated_key : str = os.path.join(BUCKET_SUB, key.split("/", 1)[-1].replace(".json.gz", ".parquet"))

    output : dict = s3_loader.upload(
        body = buffer.getvalue(),
        key = curated_key
    )

    return {
        "status": "success",
        "input": input,
        "output": output
    }