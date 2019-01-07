#!/usr/bin/env python3
import csv
import sys

# read data from STDIN and split on each newline
data = sys.stdin.read().splitlines()

# use python's csv library to create a csv reader and a writer
reader = csv.DictReader(data)
writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)

# write the header (first line of the csv)
writer.writeheader()

# loop through the rows in the original csv
for row in reader:
	# filter rows
    if row['CATEGORY'] == 'PERSONNEL COMPENSATION' and float(row['AMOUNT']) > 5000 and float(row['YEAR']) < 2017:
    	# write rows that match above filter
        writer.writerow(row)