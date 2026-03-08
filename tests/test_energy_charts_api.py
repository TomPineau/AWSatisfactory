from awsatisfactory.data_sources.EnergyChartsAPI import EnergyChartsAPI
from awsatisfactory.data_sources.EnergyChartsAPI import DATASET, BIDDING_ZONE

def test_energy_charts_api() -> None:
    energy_charts_api: EnergyChartsAPI = EnergyChartsAPI(DATASET, BIDDING_ZONE)
    data: dict = energy_charts_api.fetch_data()
    assert "data" in data
    assert "meta" in data