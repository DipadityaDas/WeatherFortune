from requests import get
from json import loads
from datetime import datetime
from bs4 import BeautifulSoup as bs


def weather_data(x):
    r = get(
        "https://www.weather-forecast.com/locations/"+x+"/forecasts/latest")

    forecast = bs(r.content, "lxml")
    latitude = forecast.find("span", {"class": "latitude"}).text
    longitude = forecast.find("span", {"class": "longitude"}).text
    day_name = datetime.now().strftime("%a")
    day_date = datetime.now().strftime("%d")
    temp = forecast.find_all("span", {"class": "temp b-forecast__table-value"})
    max_temp = temp[0].text
    min_temp = temp[36].text
    prediction = forecast.find("span", {"class": "phrase"}).text

    y = dict(loads(get("http://api.openweathermap.org/data/2.5/weather?q=" +
                       str(x).capitalize()+"&appid=3881348223779479ede078d9c8a5e2b0").content))
    pressure = str(y['main']['pressure'])
    humidity = str(y['main']['humidity'])
    wind = str(round(y['wind']['speed'] * 3.6, 3))

    if float(wind) > 100.0:
        cyclone = "Yes"
    else:
        cyclone = "No"

    return {"city": str(x).capitalize(),
            "latitude": latitude,
            "longitude": longitude,
            "day_date": day_date,
            "day_name": day_name,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "humidity": humidity,
            "pressure": pressure,
            "wind": wind,
            "prediction": prediction,
            "cyclone": cyclone}
    # print(data)


# if __name__ == "__main__":
# 	weather_data("KolKata")
