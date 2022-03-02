import requests
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from twilio.rest import Client

dm = DataManager()

fd = FlightData(dm)
lowest_price_list = fd.get_flight_data()

account_sid = "AC5d5d1d3bed511b084991b20279367956"
auth_token = "eefb63b26281d65c6597c8b726932165"

for item in lowest_price_list:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= f"{item[0]} {item[1]} {item[2]}",
        from_='+18596952590',
        to='+821023309854'
    )
    print(message.status)