"""Script for analyzing financial records, used pandas and functions to practice."""
import pandas as pd
import numpy as pd


path_write = "PyBank/Resources/Profit_Report.txt"


def header():
    """Gives the app a header."""
    print("------------------------")
    print("Financial Analysis\n")
    print("------------------------")


def importing_csv():
    """imports the csv using pandas saves as data"""

    data = pd.read_csv(
        r"PyBank/Resources/budget_data.csv"
    )
    # print(data)
    return data


def total_months(data):
    """ Calculates the total number of months using pandas count"""

    count_months = data["Date"].count()
    print(f"Total Months: {count_months}")
    return count_months


def profits_losses(data):
    """Sums up the total amount of profits and losses"""

    sum_p_l = data["Profit/Losses"].sum()
    return sum_p_l


def calc_changes(data, sum_p_l):
    """Calculate the average change."""
    profits = []
    losses = []
    #total_changes = 0

    data['changes'] = data['Profit/Losses'].diff()
    total_changes = data['changes'].sum
    print(total_changes)

    # loop through the rows to find the values
    #for row in range(1, len(data)):
        #total_changes += 
   



def increase_decreases(data):
    # Using DataFrame.query() method extract column values.
    #df2=df.query('Fee == 25000')['Courses']
    #print(df2)
    for row in range(0, len(data)):
        largest = data.nlargest(1, "Profit/Losses")
    print(f"Greatest Increase in Profits:{largest}")


def main():
    header()

    data = importing_csv()
    #print(data.info())

    total_months(data)

    sum_p_l = profits_losses(data)
    print(f'Total: ${sum_p_l}')

    calc_changes(data, sum_p_l)
    sums = data.select_dtypes(pd.np.number).sum().rename('total')
    data.loc['total'] = data.select_dtypes(pd.np.number).sum()
    print("\n")
    #increase_decreases(data)
    


main()
#completeName = os.path.join(save_path, name_of_file+".txt")         

with open(path_write, "w") as f:
    f.write("\n")
