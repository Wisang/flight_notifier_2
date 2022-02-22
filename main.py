import requests

from twilio.rest import Client

sheety_endpoint = "https://api.sheety.co/b11e9ee43e97ab01dec13f717b53914f/flightDealsSample/prices"

SHEETY_TOKEN = "Bearer d2lzYW5nOmJuVnNiRHB1ZFd4cw"
FLIGHT_SEARCH_KEY = "lAwUkoUL72fXEVrFROaWQoHMgfH0xTH8"
flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

account_sid = "AC5d5d1d3bed511b084991b20279367956"
auth_token = "ed5c8d1fef5c6be30de6f9c36bb8a6ca"

sheety_header = {
    "Authorization": SHEETY_TOKEN
}

flight_header = {
    "apikey": FLIGHT_SEARCH_KEY,
}

# flight_body = {
#     "fly_from": "ICN",
#     "fly_to": "MIA",
#     "dateFrom": "22/02/2022",
#     "dateTo": "23/02/2022",
# }

response = requests.get(url=sheety_endpoint, headers=sheety_header)
price_data = response.json()["prices"]

city_lowest_price = {item["iataCode"]: item["lowestPrice"]
                     for item in price_data}

print(city_lowest_price)

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
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"to {item['cityTo']} is ${item['price']} on {item['route'][0]['last_seen']}",
                from_='+18596952590',
                to='+821023309854'
            )
            print(message.status)
