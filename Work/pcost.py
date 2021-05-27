# pcost.py
#
# Exercise 2.15

import csv
import sys


def portfolio_cost(filename):
    """computes the price of shares listed in a csv file

    Args:
        filename (str): the path of the csv file

    Returns:
        float: the price of the shares in the file
    """
    total_price = 0

    with open(filename, 'rt') as f:
        lines = csv.reader(f)   # read the file and parse it
        header = next(lines)    # skip the header line

        for idx, line in enumerate(lines):  # loop over lines
            stock_name, shares_num, stock_price = line
            try:
                total_price += int(shares_num) * float(stock_price)
            except ValueError:
                # we can raise a warning instead using "raise Warning(msg)"
                print(f'Row {idx+1}: Missing Field encountered: {line}')

    return total_price

# grab the filename form the terminal
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:0.2f}')