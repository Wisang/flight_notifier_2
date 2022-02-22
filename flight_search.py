import requests

class FlightSearch:
    def __init__(self, fd):
        self.FLIGHT_SEARCH_KEY = "lAwUkoUL72fXEVrFROaWQoHMgfH0xTH8"
        self.flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.flight_header = {
            "apikey": self.FLIGHT_SEARCH_KEY,
        }
        self.fd = fd

    def get_flight_data(self):
        response = requests.get(
            url=self.flight_search_endpoint,
            headers=self.flight_header,
            params=self.fd.get_flight_data())
        data = response.json()["data"]
        req_data = [item["cityTo"] for item in data]
        return req_data