import requests

api_key = "abd741366c5e4a6927cfca599cfddb0d"
api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Write your city: ")

response = requests.get(
    url = api_url,
    params={
        "q" : "New York",
        "appid" : api_key,
        "units" : "metric"
    }
)
weather_data = response.json()
print(city, "temparature is", weather_data['main']['temp'])