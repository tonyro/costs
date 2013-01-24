# Main program to implement the logic of costs calculation
# Please, read Spec.txt for details of logic, file format etc.

import lib

file_path = '/home/tonyr/Work/Costs/Data/costs_20121207.csv'
raw_list = []

# Read data from file and put it in list
raw_list = lib.read_file(file_path)

# Calculate total costs for certain day
day_total = lib.get_day_total(raw_list)

print(day_total)

# Add total day costs to the day's file
lib.log_to_file(file_path, day_total)

