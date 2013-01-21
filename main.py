# Main program to implement the logic of costs calculation
# Please, read Spec.txt for details of logic, file format etc.

import lib

file_path = '/home/nurka/Stat/Costs/2012/10/06/costs_20121006.txt'
raw_list = []

# Read data from file and put it in list
raw_list = read_file(file_path)

# Calculate total costs for certain day
day_total = get_day_total(raw_list)

print(day_total)

# Add total day costs to the day's file
log_to_file(file_path, day_total)

