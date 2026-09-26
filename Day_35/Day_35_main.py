import requests
import time

"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={API key}"

OW_Website = 'https://api.openweathermap.org/data/2.5/weather'
Params = {
    "appid": "896d56366e90b35ca45205f00c3687c1",
    "lat" : 39.7392,
    "lon":-104.990


}

r = requests.get(OW_Website, params=Params)
print(r.json())
