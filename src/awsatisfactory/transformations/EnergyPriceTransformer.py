import json
import gzip
import pandas as pd
from pandas import DataFrame

class EnergyPriceTransformer :

    # Methods

    def transform(self, data : dict) -> bytes :

        df : DataFrame = pd.DataFrame({
            "timestamp": data["unix_seconds"],
            "price": data["price"]
        })

        df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")

        json_lines : str = "\n".join(json.dumps(r) for r in df)

        # compression gzip
        compressed_data : bytes = gzip.compress(json_lines.encode("utf-8"))

        return compressed_data