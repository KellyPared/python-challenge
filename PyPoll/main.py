"""Script for analyzing financial records, used pandas and functions to practice."""
import pandas as pd

path_write = "PyPoll/Resources/Profit_Report.txt"


def header():
    """Gives the app a header."""

    print("Financial Analysis\n")
    print("------------------------")


def importing_csv():
    """imports the csv using pandas saves as data"""

    data = pd.read_csv(
        r"/...PyPoll/Resources/election_data.csv"
    )
    print(data)
    return data