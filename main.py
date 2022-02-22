import requests

sheety_endpoint = "https://api.sheety.co/b11e9ee43e97ab01dec13f717b53914f/flightDealsSample/prices"

SHEETY_TOKEN = "Bearer d2lzYW5nOmJuVnNiRHB1ZFd4cw"
FLIGHT_SEARCH_KEY = "lAwUkoUL72fXEVrFROaWQoHMgfH0xTH8"
flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"


sheety_header = {
  "Authorization": SHEETY_TOKEN
}

flight_header = {
  "apikey": FLIGHT_SEARCH_KEY,
}

flight_body = {
  "fly_from": "LGA",
  "fly_to": "MIA",
  "dateFrom": "22/02/2022",
  "dateTo": "23/02/2022",
}

response = requests.get(url=sheety_endpoint, headers=sheety_header)
# print(response.json())

response = requests.get(url=flight_search_endpoint, headers=flight_header, params=flight_body)

data_list = response.json()["data"]

price_list = [{item["cityTo"]: int(item["price"])} for item in data_list]

print(price_list)
