import pandas as pd
import folium

data = pd.read_csv("locations_with_coordinates.csv")

map_center = [data['0'].mean(), data['1'].mean()]
map_object = folium.Map(location=map_center, zoom_start=5)

for _, row in data.iterrows():
    if not pd.isna(row['0']) and not pd.isna(row['1']):
        folium.Marker(
            location=[row['0'], row['1']],
            icon=folium.Icon(color="red", icon="info-sign"),
            popup=f"{row['2']}", 

        ).add_to(map_object)

map_object.save("map_of_locations.html")

map_object