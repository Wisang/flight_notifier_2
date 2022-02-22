import requests


class FlightData:
    def __init__(self):
        self.FLIGHT_SEARCH_KEY = "lAwUkoUL72fXEVrFROaWQoHMgfH0xTH8"
        self.flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.flight_header = {
            "apikey": self.FLIGHT_SEARCH_KEY,
        }

        self.flight_body = {
            "fly_from": "ICN",
            "fly_to": "MIA",
            "dateFrom": "22/02/2022",
            "dateTo": "23/02/2022",
        }

    def get_flight_data(self):
        response = requests.get(url=self.flight_search_endpoint, headers=self.flight_header, params=self.flight_body)
        data = response.json()["data"]
        req_data = [item["cityTo"] for item in data]
        return req_data
