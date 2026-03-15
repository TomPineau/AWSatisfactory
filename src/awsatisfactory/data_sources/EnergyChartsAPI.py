import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from awsatisfactory.config.config import RAW_URL, DATASET, BIDDING_ZONE


class EnergyChartsAPI:

    # Constructor

    def __init__(self, dataset: str = DATASET, bidding_zone: str = BIDDING_ZONE) -> None:
        self.dataset: str = dataset
        self.bidding_zone: str = bidding_zone
        self.session: requests.Session = self._create_session()

    # Private methods

    def _create_session(self) -> requests.Session:

        retry_strategy : Retry = Retry(
            total = 5,
            backoff_factor = 2,
            status_forcelist = [429, 500, 502, 503, 504],
            allowed_methods = ["GET"],
        )

        adapter : HTTPAdapter = HTTPAdapter(max_retries = retry_strategy)

        session : requests.Session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        return session

    # Getters and setters

    def get_dataset(self) -> str:
        return self.dataset

    def set_dataset(self, value) -> None:
        self.dataset: str = value

    def get_bidding_zone(self) -> str:
        return self.bidding_zone

    def set_bidding_zone(self, value) -> None:
        self.bidding_zone: str = value

    def get_session(self) -> requests.Session:
        return self.session
    
    def set_session(self, value) -> None:
        self.session: requests.Session = value

    # Methods

    @property
    def url(self) -> str:
        return f"{RAW_URL}/{self.dataset}?bzn={self.bidding_zone}"

    def fetch_data(self) -> dict:

        try :
            response : requests.Response = self.get_session().get(self.url, timeout = 10)
            response.raise_for_status()
            data: dict = response.json()
            return data

        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while fetching data from {self.url}: {e}")