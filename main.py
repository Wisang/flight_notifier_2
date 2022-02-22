import requests
from flight_data import FlightData

from data_manager import DataManager

account_sid = "AC5d5d1d3bed511b084991b20279367956"
auth_token = "ed5c8d1fef5c6be30de6f9c36bb8a6ca"

dm = DataManager()
city_data = dm.get_data()

fd = FlightData()
flights = fd.get_flight_data()

print(flights)

for key in city_lowest_price:
    flight_body = {
        "fly_from": "ICN",
        "fly_to": key,
        "dateFrom": "22/02/2022",
        "dateTo": "23/02/2022",
    }
    response = requests.get(url=flight_search_endpoint, headers=flight_header, params=flight_body)
    data_list = response.json()["data"]
    for item in data_list:
        if city_lowest_price[key] > int(item["price"]):
            print(f"to {item['cityTo']} is ${item['price']} on {item['route'][0]['last_seen']}")

