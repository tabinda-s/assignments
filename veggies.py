import csv


vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

name_field = 'name'
color_field = 'color'
name_length_field = 'name_length'

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow([name_field, color_field, name_length_field])

    # now iterate over the vegetables (which is an array)
    # each item in the array is a dictionary
    for veg_dict in vegetables:

        # set variables with the corresponding information
        veg_name = veg_dict[name_field]
        veg_color = veg_dict[color_field]
        veg_name_length = len(veg_name)

        # now write the output from the dictionary
        writer.writerow([veg_name, veg_color, veg_name_length])
        