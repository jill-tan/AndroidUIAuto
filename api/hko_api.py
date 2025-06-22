import requests
from datetime import datetime, timedelta

def get_forecast_data():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None

def get_humidity_day_after_tomorrow(api_data):
    today = datetime.now().date()
    target_date = today + timedelta(days=2)
    target_str = target_date.strftime("%Y%m%d")

    for item in api_data.get("weatherForecast", []):
        if item.get("forecastDate") == target_str:
            min_rh = item.get("forecastMinrh", {}).get("value")
            max_rh = item.get("forecastMaxrh", {}).get("value")
            if min_rh and max_rh:
                return f"{min_rh} - {max_rh}%"
    return None
