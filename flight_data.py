import requests


class FlightData:
    def __init__(self):
        self.flight_body = {
            "fly_from": "ICN",
            "fly_to": "MIA",
            "dateFrom": "22/02/2022",
            "dateTo": "23/02/2022",
        }

    def get_flight_data(self):
        return self.flight_body
