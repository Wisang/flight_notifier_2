from twilio.rest import Client

class NotificationManager:
    pass

# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     body=f"to {item['cityTo']} is ${item['price']} on {item['route'][0]['last_seen']}",
#     from_='+18596952590',
#     to='+821023309854'
# )
# print(message.status)