import json

# read file
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

data = []

# define members
members = superheroes['members']

# loop through members and list powers
for member in members:
	powers = member['powers']

# loop through powers and print
	for power in powers:
		data.append(power)

unique_powers = set(data)
unique_powers_list = list(unique_powers)
print(unique_powers_list)