#Read vegetables.csv into a variable called vegetables.
import csv

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
  
#Loop through vegetables and filter down to only green vegtables using a whitelist.

green_vegetables = []
whitelist = ['green']
for row in rows:
	if row ['color'] in whitelist:
		green_vegetables.append(row)

print(green_vegetables)
