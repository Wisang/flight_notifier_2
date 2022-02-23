from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.account_sid = "AC5d5d1d3bed511b084991b20279367956"
        self.auth_token = "ed5c8d1fef5c6be30de6f9c36bb8a6ca"

# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     body=f"to {item['cityTo']} is ${item['price']} on {item['route'][0]['last_seen']}",
#     from_='+18596952590',
#     to='+821023309854'
# )
# print(message.status)