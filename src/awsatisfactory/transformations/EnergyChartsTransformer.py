import gzip
import json


class EnergyChartsTransformer :

    # Methods
    
    def to_records(self, data: dict) -> list[dict]:

        timestamps = data["unix_seconds"]
        prices = data["price"]

        records = []

        for timestamp, price in zip(timestamps, prices):
            records.append(
                {
                    "unix_seconds": timestamp,
                    "price": price
                }
            )

        json_lines : str = "\n".join(json.dumps(r) for r in records)

        # compression gzip
        compressed_data : bytes = gzip.compress(json_lines.encode("utf-8"))

        return compressed_data