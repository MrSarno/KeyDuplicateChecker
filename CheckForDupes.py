# John Sweeney
# 7-June-2019

# Basic Python file to check a list of keys for duplicates, and remove them
# Version 1.0

import collections, csv

keys_list = []

with open('keys.csv', 'r') as the_input, open('no_dupes.csv', 'w', newline='') as the_output:

    reader = csv.reader(the_input, skipinitialspace=True)
    writer = csv.writer(the_output, delimiter=',')

    for row in reader:
        if row not in keys_list:
            keys_list.append(row)

    for item in keys_list:
        writer.writerow(item)