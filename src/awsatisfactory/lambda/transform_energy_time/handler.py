import json
import gzip
import boto3
import pandas as pd
import urllib.parse
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
from io import BytesIO

s3 = boto3.client("s3")

RAW = "raw"
CURATED = "curated"


def lambda_handler(event, context) -> dict :

    record : dict = event["Records"][0]

    bucket : str = record["s3"]["bucket"]["name"]
    key : str = record["s3"]["object"]["key"]
    key = urllib.parse.unquote_plus(key)  # Decode URL-encoded key

    response : dict = s3.get_object(Bucket = bucket, Key = key)
    compressed_file : bytes = response["Body"].read()

    rows : list = []

    with gzip.GzipFile(fileobj = BytesIO(compressed_file)) as f:
        for line in f :
            row = json.loads(line)

            row["unix_seconds"] = int(row["unix_seconds"])
            row["price"] = float(row["price"])
            row["datetime"] = datetime.fromtimestamp(row["unix_seconds"])
            rows.append(row)
            for _key, value in row.items():
                print(f"{_key} of type {type(value)} and value {value}")

    schema = pa.schema([
        ("unix_seconds", pa.int64()),
        ("price", pa.float64()),
        ("datetime", pa.timestamp("ms"))
    ])

    print(type(schema))

    table = pa.Table.from_pylist(rows, schema = schema)

    buffer : BytesIO = BytesIO()

    pq.write_table(
        table,
        buffer,
        compression = "snappy"
    )

    curated_key : str = key.replace(RAW, CURATED).replace(".json.gz", ".parquet")

    s3.put_object(
        Bucket = bucket,
        Key = curated_key,
        Body = buffer.getvalue()
    )

    return {
        "status": "success",
        "input_file": key,
        "output_file": curated_key
    }