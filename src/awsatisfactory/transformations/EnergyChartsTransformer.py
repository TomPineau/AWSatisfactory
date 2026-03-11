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

        return records