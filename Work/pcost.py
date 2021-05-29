# pcost.py
#
# Exercise 3.14

import csv
import sys
import report


def portfolio_cost(filename):
    """computes the price of shares listed in a csv file

    Args:
        filename (str): the path of the csv file

    Returns:
        float: the price of the shares in the file
    """
    total_price = 0

    portfolio = report.read_portfolio(filename)
    
    for idx, record in enumerate(portfolio):  # loop over lines
        # no need to catch exceptions because the imported module handles that
        total_price += int(record['shares']) * float(record['price'])
    
    return total_price

# grab the filename form the terminal
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:0.2f}')