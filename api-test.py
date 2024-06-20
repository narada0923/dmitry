import requests

api_key = 'f78ceda4749c6d73414fccce4962386c'
url = 'http://api.agromonitoring.com/agro/1.0/soil'
params = {
    'lat': 47.60883167,
    'lon': 96.45385333,
    'appid': api_key
}

response = requests.get(url, params=params)
if response.status_code == 200:
    soil_data = response.json()
    print(soil_data["t0"] - 273.15, soil_data["moisture"]) 
else:
    print("Failed to retrieve data:", response.status_code)
    print(0, 0)
    