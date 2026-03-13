from awsatisfactory.data_sources.EnergyChartsAPI import EnergyChartsAPI
from awsatisfactory.storage.RawLoader import RawLoader
from awsatisfactory.storage.CuratedLoader import CuratedLoader
from awsatisfactory.transformations.EnergyTimeTransformer import EnergyTimeTransformer


class EnergyChartPipeline:

    def run(self):

        api = EnergyChartsAPI()

        raw_loader = RawLoader("energy-data-lake")
        transformer = EnergyTimeTransformer()
        curated_loader = CuratedLoader("energy-data-lake")

        data = api.fetch()

        raw_loader.upload(data, "price", "energy_charts")

        df = transformer.transform(data)

        curated_loader.upload(df)