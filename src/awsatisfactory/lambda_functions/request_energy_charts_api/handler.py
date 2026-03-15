from datetime import datetime

from awsatisfactory.data_sources.EnergyChartsAPI import EnergyChartsAPI, DATASET, BIDDING_ZONE
from awsatisfactory.transformations.EnergyChartsTransformer import EnergyChartsTransformer
from awsatisfactory.storage.S3Loader import S3Loader
from awsatisfactory.config.config import BUCKET_SUB, ENERGY_CHARTS, PRICE


def lambda_handler(event, context) -> dict:

    s3_loader = S3Loader()
    api = EnergyChartsAPI(DATASET, BIDDING_ZONE)
    transformer = EnergyChartsTransformer()

    file_extension : str = ".json.gz"
    date : datetime = datetime.now()
    key = (
            f"{BUCKET_SUB}/"
            f"{ENERGY_CHARTS}/"
            f"{PRICE}/"
            f"year={date.year}/"
            f"month={date.month:02}/"
            f"day={date.day:02}/"
            f"data_{date.strftime('%Y%m%dT%H%M%S')}"
            f"{file_extension}"
        )

    try :
        data = api.fetch_data()
        records = transformer.to_records(data)
        result : str = s3_loader.upload(records, key)

        return {
            "status": "success",
            "output": result
        }
    
    except Exception as e:
        raise Exception(f"EnergyCharts ingestion failed: {str(e)}")