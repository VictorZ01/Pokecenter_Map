# Pokecenter_Map

This project is a Python-based map for the purpose of plotting all Pokemon Center Vending Machines. Copy and paste the addresses that are desired into the data variable inside of the `Address_scraper.py`. Then run 
Address_Scrapper.py, map_CA.py and Map.py to generate an html file. Automation with a scrapper did not work, but further work with Selenium might. 

---

## Features

- **Data Input:** Reads address data from a CSV file.
- **Geocoding:** Converts addresses into latitude and longitude using the `geopy` library.
- **Interactive Map:** Plots the geocoded addresses on an interactive map using `folium`.
- **Output:** Saves the enhanced dataset (with coordinates) to a new CSV file and generates an HTML file for the interactive map.

---

## Requirements

- Python 3.8+
- Required libraries:
  - `pandas`
  - `geopy`
  - `folium`

Install the required libraries using:
```bash
pip install pandas geopy folium