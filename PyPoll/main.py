import os
import csv

PyBank_csv = os.path.join("PyPoll/Resources/election_data.csv")
path_write = "PyPoll/Resources/"
completeName = os.path.join(path_write, "election_data.txt") 


# Lists to store data
total_number_votes = []
list_candidates = []

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(PyBank_csv) as data:
    data = csv.reader(data, delimiter=",")
    next(data)
    
    for row in data:
        # add all months to list
        total_number_votes.append(row[0])
        if row[1] in list_candidates:
            continue
        else:
            list_candidates.append(row[1])

print(len(total_number_votes))
print(list_candidates)