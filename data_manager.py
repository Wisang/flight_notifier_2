import requests


class DataManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/b11e9ee43e97ab01dec13f717b53914f/flightDealsSample/prices"
        self.SHEETY_TOKEN = "Bearer d2lzYW5nOmJuVnNiRHB1ZFd4cw"

        self.sheety_header = {
            "Authorization": self.SHEETY_TOKEN
        }

        self.flight_body = {
            "fly_from": "ICN",
            "fly_to": "MIA",
            "dateFrom": "22/02/2022",
            "dateTo": "23/02/2022",
        }

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_header)
        price_data = response.json()["prices"]
        city_lowest_price = {item["iataCode"]: item["lowestPrice"] for item in price_data}
        return city_lowest_price
