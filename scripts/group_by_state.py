import json
from collections import defaultdict

input_file = "files/locations.json"
output_file = "files/locations_by_state.json"

with open(input_file, "r", encoding="utf-8") as f:
    locations = json.load(f)

grouped = defaultdict(list)
for loc in locations:
    state = loc.get("state", "Unknown")
    grouped[state].append(loc)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dict(grouped), f, ensure_ascii=False, indent=2)

print(f"Grouped locations saved to {output_file}")
