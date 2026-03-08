from awsatisfactory.simulation.run_simulation import run_simulation
from awsatisfactory.data_sources.EnergyChartsAPI import EnergyChartsAPI
from awsatisfactory.data_sources.EnergyChartsAPI import DATASET, BIDDING_ZONE
from awsatisfactory.transformations.EnergyPriceTransformer import EnergyPriceTransformer

from pandas import DataFrame


def main() -> None:
    # run_simulation()
    energy_charts_api: EnergyChartsAPI = EnergyChartsAPI(DATASET, BIDDING_ZONE)
    transformer: EnergyPriceTransformer = EnergyPriceTransformer()
    data: dict = energy_charts_api.fetch_data()
    transformed_data: DataFrame = transformer.transform(data)
    print(transformed_data.loc[transformed_data["datetime"].idxmin()], transformed_data.loc[transformed_data["datetime"].idxmax()])


if __name__ == "__main__":
    main()
