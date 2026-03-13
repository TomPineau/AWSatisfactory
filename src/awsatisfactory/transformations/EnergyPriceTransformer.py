import pandas as pd
from pandas import DataFrame

class EnergyPriceTransformer :

    # Methods

    def transform(self, data : dict) -> DataFrame :

        df : DataFrame = pd.DataFrame({
            "timestamp": data["unix_seconds"],
            "price": data["price"]
        })

        df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")

        return df