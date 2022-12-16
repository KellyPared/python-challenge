'''Script for analyzing financial records'''


import pandas as pd

path_write = ('PyPoll/Resources/Profit_Report.txt')

def header():
    '''Gives the app a header.'''
    
    print("Financial Analysis")
    print("------------------------")
    
    
def importing_csv():
    '''imports the csv using pandas saves as df'''
    
    df = pd.read_csv(r'/Users/kellypared/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv')
    #print(df)
    return df


def total_months(df):
    ''' Calculates the total number of months using pandas count'''
    
    count_months = df['Date'].count()
    print(f"Total Months: {count_months}")
    return count_months
    

def profits_losses(df):
    '''Sums up the total amount of profits and losses'''

    sum_p_l = df['Profit/Losses'].sum()
    print(f'Total: ${sum_p_l/86}')
    return sum_p_l


def average_change(df):
    '''Calculate the average change.'''

    avg_change = df['Profit/Losses'].std()
    print(avg_change)


def increase_decreases(df):
    print(df['Profit/Losses'].max())



def main():
    header()
    data = importing_csv()
    count = total_months(data)
    sum_p_l = profits_losses(data)
    average_change(data)
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