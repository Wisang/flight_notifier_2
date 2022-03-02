import requests
import datetime as dt


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
            "dateFrom": dt.datetime.now().strftime("%d/%m/%Y"), #"02/03/2022",
            "dateTo": (dt.datetime.now()+dt.timedelta(days=60*3)).strftime("%d/%m/%Y"), #02/09/2022",
            "curr": "GBP",
            "max_stopovers": 0,
            "one_for_city": 1,
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
            for city_data in response.json()["data"]:
                self.total_data.append((city_data["cityTo"], city_data["local_departure"].split("T")[0], city_data["price"]))
        return self.total_data
