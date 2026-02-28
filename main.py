import requests
import os

PARAMETERS = {
   "lat": 41.8832,
   "lon": -87.6324,
   "appid": os.environ.get("OPEN_WEATHER_API_KEY"),
   "cnt": 4
}

data = None
need_umbrella = False

try:
   response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=PARAMETERS)
   response.raise_for_status()
   data = response.json()
   
except requests.exceptions.HTTPError as error:
   print("Error occurred:", error)
   data = {"error": str(error)}

if data and "list" in data:
   for list_item in data["list"]:
      for weather_item in list_item["weather"]:
          if weather_item["id"] < 700:
              need_umbrella = True

print(need_umbrella)

PARAMETERS_SMS = {
   "phone": os.environ.get("NUMBER"),
   "text": "Bring your umbrella.",
   "apikey": os.environ.get("RON_API_KEY")
}
if need_umbrella:
   response_sms = requests.get(url="https://api.callmebot.com/whatsapp.php", params=PARAMETERS_SMS)

