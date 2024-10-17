import requests
import time
import json
from temperature_conversion import convert_temperature
from rollup_aggregates import calculate_daily_summary
from alerts import monitor_alerts

API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "4df071f9fe5122f051f8804e21c7eda8"  # Sign up for an API key

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather(city):
    """Fetch real-time weather data from OpenWeatherMap API"""
    params = {'q': city, 'appid': API_KEY}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data for {city}: {response.status_code}")

def get_weather_for_all_cities():
    """Fetch weather data for all configured cities"""
    weather_data = {}
    for city in CITIES:
        try:
            weather_data[city] = fetch_weather(city)
        except Exception as e:
            print(e)
        time.sleep(1)  # Pause to avoid API rate limits
    return weather_data

def main():
    while True:
        weather_data = get_weather_for_all_cities()
        # Process and evaluate weather data
        # Call other functions for processing, alerts, etc.
        time.sleep(300)  # 5-minute interval

if __name__ == "__main__":
    main()
