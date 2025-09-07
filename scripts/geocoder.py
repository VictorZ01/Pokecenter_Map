import json
import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
input_file = "files/addresses.csv"
output_file = "files/locations.json"

def geocode_google(address, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] == "OK":
        loc = data["results"][0]["geometry"]["location"]
        return loc["lat"], loc["lng"]
    return None, None

with open(input_file, "r", encoding="utf-8") as f:
    addresses_dict = json.load(f)

locations = []

for state, addresses in addresses_dict.items():
    for address in addresses:
        lat, lng = geocode_google(address, API_KEY)
        if lat and lng:
            locations.append({
                "state": state,
                "address": address,
                "lat": lat,
                "lng": lng
            })
            print(f"Geocoded: {address} -> {lat}, {lng}")
        else:
            print(f"Not found: {address},{lat},{lng}")
        time.sleep(0.1)  # Be kind to the API!

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(locations, f, ensure_ascii=False, indent=2)

print(f"Saved {len(locations)} locations to {output_file}")