import requests
from requests import module

# Constants

RAW_URL : str = "https://api.energy-charts.info"
DATASET : str = "price"
BIDDING_ZONE : str = "FR"

# Constructor

class EnergyCharts :

    def __init__(self, dataset : str, bidding_zone : str) -> None :
        self.dataset : str = dataset
        self.bidding_zone : str = bidding_zone

    # Getters and setters

    def get_dataset(self) -> str :
        return self.dataset
    
    def set_dataset(self, value) -> None :
        self.dataset : str = value

    def get_bidding_zone(self) -> str :
        return self.bidding_zone
    
    def set_bidding_zone(self, value) -> None :
        self.bidding_zone : str = value

    # Methods

    @property
    def url(self) -> str :
        return f"{RAW_URL}/{self.dataset}?bzn={self.bidding_zone}"

    def fetch_data(self) -> None :
        response : module = requests.get(self.url)
        response_status_code : int = response.status_code

        if response_status_code == 200 :
            data : dict = response.json()
            return data
        else :
            raise Exception(f"Failed to fetch data from {self.url} with status code {response_status_code}")