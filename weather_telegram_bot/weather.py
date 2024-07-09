import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

def get_weather(x, y):
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": x,
        "longitude": y,
        "current": ["temperature_2m", "is_day", "cloud_cover", "wind_speed_10m"],
	    "timezone": "Europe/Moscow"
    }
    response = openmeteo.weather_api(url, params=params)[0]
    current = response.Current()


    #debug
    # print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    # print(f"Elevation {response.Elevation()} m asl")
    # print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    # print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Current values. The order of variables needs to be the same as requested.
    # current_temperature_2m = current.Variables(0).Value()
    # current_is_day = current.Variables(1).Value()
    # current_cloud_cover = current.Variables(2).Value()
    # current_wind_speed_10m = current.Variables(3).Value()

    # print(f"Current time {current.Time()}")
    # print(f"Current temperature_2m {current_temperature_2m}")
    # print(f"Current is_day {current_is_day}")
    # print(f"Current cloud_cover {current_cloud_cover}")
    # print(f"Current wind_speed_10m {current_wind_speed_10m}")
    return current


if __name__ == "__main__":
    get_weather(55.7887, 49.1221)