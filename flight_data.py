import requests


class FlightData:
    def __init__(self, data_manager):
        self.FLIGHT_SEARCH_KEY = "lAwUkoUL72fXEVrFROaWQoHMgfH0xTH8"
        self.flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.flight_header = {
            "apikey": self.FLIGHT_SEARCH_KEY,
        }
        self.flight_body = {
            "fly_from": "LON",
            "fly_to": "MIA",
            "dateFrom": "25/02/2022",
            "dateTo": "26/02/2022",
        }
        self.dm = data_manager
        self.total_data = []

    def get_flight_data(self):
        for item in self.dm.get_data():
            self.flight_body["fly_to"] = item
            response = requests.get(
                url=self.flight_search_endpoint,
                headers=self.flight_header,
                params=self.flight_body)
            data = [(item["cityTo"], item["local_departure"], item["price"]) for item in response.json()["data"]]
            self.total_data.append(data)
        return self.total_data
