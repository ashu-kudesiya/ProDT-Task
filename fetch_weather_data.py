# fetch_weather_task.py

import requests

def fetch_weather_data(api_key, location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    data = response.json()
    return data
