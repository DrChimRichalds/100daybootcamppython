import requests

import os
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

# Wichita KS 37°68'N / 98°39'W
#DEnver CO "lat" : 39.7392,
    # "lon":-104.990,
OW_Website = 'https://api.openweathermap.org/data/2.5/forecast'
Params = {
    "appid": "896d56366e90b35ca45205f00c3687c1",
    "lat" : 37.68,
    "lon":-97.335571,
    "cnt": 4

}

TWILIO_ACCOUNT_SID = os.environ.get("twilio_account_SID")
TWILIO_AUTH_TOKEN = os.environ.get("twilio_account_TOKEN")
print(TWILIO_AUTH_TOKEN)
print(TWILIO_ACCOUNT_SID)

r = requests.get(OW_Website, params=Params)
r.raise_for_status()

will_rain = False
for items in r.json()['list']:
    if items['weather'][0]['id'] < 700:
        will_rain = True
        print(f"at the following time {items['dt_txt']} the weather will be poor because of {items['weather'][0]['description']}")
if will_rain:
    print(f"The weather will be poor because of rain in the next {r.json()['cnt']} intervals")
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        to="+13035649767",
        from_="+17372583478",
        body="sms_appointment_reminders",
    )
    print(message.status)