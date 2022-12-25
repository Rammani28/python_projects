import requests
import os

api_key = os.environ.get("API_KEY")

"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
parameters = {
    "lat": 27.717245,
    "lon": 85.323959,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()
print(data)
code = data['cod']
weather = data['main']
print(weather)