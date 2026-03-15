from awsatisfactory.data_sources.EnergyChartsAPI import EnergyChartsAPI
from awsatisfactory.transformations.EnergyChartsTransformer import EnergyChartsTransformer
from awsatisfactory.storage.S3Loader import S3Loader
from awsatisfactory.config.config import *
from datetime import datetime


def main() -> None:
    
    api = EnergyChartsAPI(DATASET, BIDDING_ZONE)
    transformer = EnergyChartsTransformer()
    date : datetime = datetime.now()

    key = (
            f"{BUCKET_SUB}/"
            f"{ENERGY_CHARTS}/"
            f"{PRICE}/"
            f"year={date.year}/"
            f"month={date.month:02}/"
            f"day={date.day:02}/"
            f"data_{date.strftime('%Y%m%dT%H%M%S')}.json.gz"
        )
    
    data = api.fetch_data()
    print(data)
    records = transformer.to_records(data)

    s3loader : S3Loader = S3Loader(BUCKET)
    s3loader.upload(records, key)


if __name__ == "__main__":
    main()
