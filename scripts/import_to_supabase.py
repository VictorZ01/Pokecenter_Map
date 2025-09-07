import json
from supabase import create_client, Client
import os 
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY") 

print(SUPABASE_KEY)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

with open("files/locations_by_state.csv", "r", encoding="utf-8") as f:
    data = json.load(f)

locations_to_insert = []

for state, locations in data.items():
    for location in locations:
        locations_to_insert.append({
            "state": state.split(" ")[0],
            "address": location["address"],
            "lat": location["lat"],
            "lng": location["lng"]
        })

batch_size = 100
for i in range(0, len(locations_to_insert), batch_size):
    batch = locations_to_insert[i:i + batch_size]
    
    try:
        result = supabase.table("PokeLocation").insert(batch).execute()
        print(f"Inserted batch {i//batch_size + 1}: {len(batch)} locations")
    except Exception as e:
        print(f"Error inserting batch {i//batch_size + 1}: {e}")

print("Import completed!")
