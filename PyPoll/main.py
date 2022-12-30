import os
import csv

#/python-challenge/PyPoll/Resources/election_data.csv
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
PyBank_csv = os.path.join(ROOT_DIR, "PyPoll", "Resources", "election_data.csv")


#absolute_path = os.path.dirname("election_data.csv")
#relative_path = "PyPoll/Resources/"

completeName = os.path.join(ROOT_DIR, "PyPoll", "Resources", "election_data.txt") 
#full_path = os.path.join(absolute_path, relative_path)

# Lists to store data
total_number_votes = []
list_candidates = []
total_votes_stockham = 0
total_votes_degette = 0
total_votes_doane = 0



with open(PyBank_csv) as data:
    data = csv.reader(data, delimiter=",")
    next(data)
    
    for row in data:
        # add all months to list
        total_number_votes.append(row[0])
       
        if row[2] =='Charles Casper Stockham':
            total_votes_stockham += 1
        elif row[2] =='Diana DeGette':
            total_votes_degette += 1
        elif row[2] == 'Raymon Anthony Doane':
            total_votes_doane += 1
        #if row[2] in list_candidates:
        #list_candidates.append(row[2])
            
total = [total_votes_degette, total_votes_doane, total_votes_stockham]
           
print('Election Results')
print('-'*25)
print(f'Total Votes: {len(total_number_votes)}')
print('-'*25)
print(f'Charles Casper Stockham: {round((total_votes_stockham/len(total_number_votes))*100,3)}% ({total_votes_stockham})')
print(f'Diana DeGette {round((total_votes_degette/len(total_number_votes))*100,3)}% ({total_votes_degette})')
print(f'Raymon Anthony Doane {round((total_votes_doane/len(total_number_votes))*100,3)}% ({total_votes_doane})')
print('-'*25)

if max(total) == total_votes_stockham:
    print('Winner: Charles Casper Stockham')
elif max(total) == total_votes_degette:
    print('Winner: Diana DeGette')
else:
    print('Winner: Raymon Anthony Doane')
print('-'*25)



#  Open the output file
with open(completeName, "w") as datafile:

    datafile.write('Election Results\n')
    datafile.write('-'*25)
    datafile.write('\n')
    datafile.write(f'Total Votes: {len(total_number_votes)}\n')
    datafile.write('-'*25)
    datafile.write('\n')
    datafile.write(f'Charles Casper Stockham: {round((total_votes_stockham/len(total_number_votes))*100,3)}% ({total_votes_stockham})')
    datafile.write('\n')
    datafile.write(f'Diana DeGette {round((total_votes_degette/len(total_number_votes))*100,3)}% ({total_votes_degette})')
    datafile.write('\n')
    datafile.write(f'Raymon Anthony Doane {round((total_votes_doane/len(total_number_votes))*100,3)}% ({total_votes_stockham})')
    datafile.write('\n')
    datafile.write('-'*25)
    datafile.write('\n')

    if max(total) == total_votes_stockham:
        datafile.write('Winner: Charles Casper Stockham')
    elif max(total) == total_votes_degette:
        datafile.write('Winner: Diana DeGette')
    else:
        datafile.write('Winner: Raymon Anthony Doane')
    datafile.write('\n')
    datafile.write('-'*25)