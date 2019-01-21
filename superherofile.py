import csv
import json

#read superheroes file
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# loop through members
members = superheroes['members']
for member in members:
	# print(member)

# save member information in csv
	with open('members.csv', 'w') as f:
		writer = csv.writer(f)
		header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
		writer.writerow(header)

		for member in members:
			row = [
				member['name'],
				member['age'],
				member['secretIdentity'],
				member['powers'],
				superheroes['squadName'],
				superheroes['homeTown'],
				superheroes['formed'],
				superheroes['secretBase'],
				superheroes['active']
			]

			writer.writerow(row)