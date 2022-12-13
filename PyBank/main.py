'''Script for analyzing financial records'''


import csv

def importing_csv():
    with open('budget_data.csv', newline='') as csvfile:
        financial_records = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in financial_records:
            print('< '.join(row))

importing_csv()

def total_months():
    # Calculates the total number of months
    
    # find the column
    pass


# Calculate the net amounth of Profits/Losses over the entire period

# Calculate the changes in Profit/Losses over the entire period and average the changes.

# The greatest increase in profit/losses(date and amount) over entire period

# The greatest decrease in profits(date and amount) over the entire period.

# print analysis to terminal
# export file as a text