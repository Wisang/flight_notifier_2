import requests
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

dm = DataManager()
city_data = dm.get_data()

print(city_data)

fd = FlightData()

# fs = FlightSearch(fd)
# flights = fs.get_flight_data()

print(fd.get_flight_data())

# for key in city_lowest_price:
#
#     response = requests.get(url=flight_search_endpoint, headers=flight_header, params=flight_body)
#     data_list = response.json()["data"]
#     for item in data_list:
#         if city_lowest_price[key] > int(item["price"]):
#             print(f"to {item['cityTo']} is ${item['price']} on {item['route'][0]['last_seen']}")

