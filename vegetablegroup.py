import csv
import json

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
from pprint import pprint

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "okra", "color": "green"},
 {"name": "corn", "color": "yellow"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

vegetables_by_color = {}

for vegetable in vegetables:
    color = vegetable['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(vegetable)
    else:
        vegetables_by_color[color] = [vegetable]

pprint(vegetables_by_color)  


#output to JSON

with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent=2)
