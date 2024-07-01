# activities.py

from temporalio import activity
from fetch_weather_data import fetch_weather_data

@activity.defn
async def fetch_weather_data_activity(api_key: str, location: str):
    return fetch_weather_data(api_key, location)
