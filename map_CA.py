import pandas as pd
from geopy.geocoders import Nominatim 
import folium 
import time 

data = pd.read_csv("locations_CA.csv")
geolocator = Nominatim(user_agent="pokemontool")
def geocode(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None 

#data['Coordinates'] = (data["Address"]+","+data["City"]).apply(lambda x:pd.Series(geocode(x)))

#data[['Latitude', 'Longitude']] = pd.DataFrame(data['Coordinates'].to_list(), index=data.index)

coords = []
for index,row in data.iterrows():
    if index % 5 ==0:
        print(index)
    address = (row["Address"]+", "+row["City"])
    latitude, longitude = geocode(address)
    if latitude == None:
        print(address)
    coords.append((latitude,longitude,address))
    time.sleep(2)

#address =  (data.iloc[0]["Address"]+","+data.iloc[0]["City"])
#latitude, longitude = geocode(address)
#print(f"Latitude: {latitude}, Longitude: {longitude}")
pd.DataFrame(coords).to_csv("locations_with_coordinates.csv", index=False)
