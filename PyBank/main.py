import os
import csv

PyBank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")
completeName = os.path.join("PyBank", "Resources", "budget_data_easy.txt") 


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

changes = ([t-s for s, t in zip(total_profit, total_profit[1:])])
average_change = sum(changes)/(len(total_number_months)-1)
max_p = max(changes)
min_p = min(changes)
month_max_index = changes.index(max_p)
month_min_index = changes.index(min_p)

month_high = (total_number_months[month_max_index+1])
month_low = (total_number_months[month_min_index+1])


print("------------------------")
print("Financial Analysis\n")
print("------------------------")
print(f'Total Months:  {len(total_number_months)}')
print(f'Total:  ${sum(total_profit)}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits: {month_high} ${max_p}')
print(f'Greatest Increase in Profits: {month_low} ${min_p}')

# Set variable for output file
output_file = os.path.join("budget_data_easy.txt")

#  Open the output file
with open(completeName, "w") as datafile:

    #datafile.writer = csv.writer(datafile)
    datafile.write("------------------------\n")
    datafile.write("Financial Analysis\n")
    datafile. write("------------------------\n")
    datafile. write(f'Total Months:  {len(total_number_months)}\n')
    datafile.write(f'Total:  ${sum(total_profit)}\n')
    datafile.write(f'Average Change: ${round(average_change, 2)}\n')
    datafile.write(f'Greatest Increase in Profits: {month_high} ${max_p}\n')
    datafile.write(f'Greatest Increase in Profits: {month_low} ${min_p}\n')

    

