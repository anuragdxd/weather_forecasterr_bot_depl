import requests
import json

API_KEY = "26e1733cea604488a77134653231301"

def weather_info(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=yes&alerts=no"
    responce = requests.get(url)
    data = responce.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    current_weather = data["current"]["condition"]["text"]
    updated = data["current"]["last_updated"]
    temp = data["current"]["temp_c"]
    maxtemp_c = data["forecast"]['forecastday'][0]['day']['maxtemp_c']
    min_temp = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
    average_temp = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    sunrise = data["forecast"]["forecastday"][0]["astro"]["sunrise"]
    sunset = data["forecast"]["forecastday"][0]["astro"]["sunset"]
    moonrise = data["forecast"]["forecastday"][0]["astro"]["moonrise"]
    moonset = data["forecast"]["forecastday"][0]["astro"]["moonset"]
    moonphase = data["forecast"]["forecastday"][0]["astro"]["moon_phase"]

    return(f"City: {city}, {country} \n\nCurrent weather condition: {current_weather} \n\nLast updated on: {updated} \n\nCurrent temprature: {temp} °C \n\nMax temprature: {maxtemp_c} °C \n\nMin temprature: {min_temp} °C \n\nAverage temprature: {average_temp} °C \n\nSunrise: {sunrise} \n\nSunset: {sunset} \n\nMoonrise: {moonrise} \n\nMoonset: {moonset} \n\nMoonphase: {moonphase}")


