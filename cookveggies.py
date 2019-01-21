#Read veggies.csv into a var "vegetables"
import csv
import json

with open('veggies.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = list(reader)

#orint the variable "vegetables"
print(vegetables)


#sabe "vegetables" as vegetables.json

with open('cookedveggies.json', 'w') as f:
	json.dump(vegetables, f, indent=2)