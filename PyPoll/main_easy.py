import os
import csv

PyBank_csv = os.path.join("PyPoll/Resources/election_data.txt")
path_write = "PyPoll/Resources/"
completeName = os.path.join(path_write, "election_data.txt") 


# Lists to store data
total_number_months = []
total_profit = []

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(PyBank_csv) as data:
    data = csv.reader(data, delimiter=",")
    next(data)
    
    for row in data:
        # add all months to list
        total_number_months.append(row[0])
        #print(total_number_months)

        # Add all p/l to list
        total_profit.append(int(row[1]))