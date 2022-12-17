'''Script for analyzing financial records, used pandas and functions to practice.'''
import pandas as pd

path_write = ('PyPoll/Resources/Profit_Report.txt')

def header():
    '''Gives the app a header.'''
    
    print("Financial Analysis")
    print("------------------------")
    
    
def importing_csv():
    '''imports the csv using pandas saves as data'''
    
    data = pd.read_csv(r'/Users/kellypared/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv')
    #print(data)
    return data


def total_months(data):
    ''' Calculates the total number of months using pandas count'''
    
    count_months = data['Date'].count()
    print(f"Total Months: {count_months}")
    return count_months
    

def profits_losses(data):
    '''Sums up the total amount of profits and losses'''

    sum_p_l = data['Profit/Losses'].sum()
    return sum_p_l


def calc_changes(data,sum_p_l):
    '''Calculate the average change.'''
    profits = []
    losses = []
    #highest_profit = 0
    #lowest_profit = 0

    #get location of of the profit/losses items
    index_profit = data.columns.get_loc('Profit/Losses')

    #loop through the rows to find the values

    for row in range(0, len(data)):
        if data.iat[row, index_profit] < 0 :
            losses.append(data.iat[row, index_profit]) 
    
        else:
            profits.append(data.iat[row, index_profit]) 
    change_pl = sum(profits)-sum(losses)
    print(change_pl)
    

    

    #print(f'Average Change: {avg_change}, data_loss')
    


def increase_decreases(data):
    print((data.nlargest(1, 'Profit/Losses')))
    


def main():
    header()
    data = importing_csv()
    print("\n")
    total_months(data)
    sum_p_l = profits_losses(data)
    calc_changes(data, sum_p_l)
    increase_decreases(data)
   

main()
with open(path_write, 'w') as f:
    f.write('\n')

  
    
 # change   



# Calculate the net amounth of Profits/Losses over the entire period

# Calculate the changes in Profit/Losses over the entire period and average the changes.

# The greatest increase in profit/losses(date and amount) over entire period

# The greatest decrease in profits(date and amount) over the entire period.

# print analysis to terminal
# export file as a text