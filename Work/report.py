# report.py
#
# Exercise 2.16


import csv
import sys

def read_portfolio(filename):
    """parses a csv file into a list of tuples

    Args:
        filename (str): the path of the csv file

    Returns:
        list: list of tuples. each tuple contains info of one line
    """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)        # parse the csv file
        headers = next(rows)        # skip the header line
        for row in rows:            # loop over lines
            # cast line contents into proper datatypes
            holding = dict(zip(headers, row))
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])
            portfolio.append(holding)

    return portfolio    


def read_prices(filename):
    """reads the stock prices from the csv file

    Args:
        filename (str): file path of the prices csv file

    Returns:
        dict: a dictionary of prices by stock name
    """
    prices = {}

    f = open(filename, 'r')    # parse the file
    rows = csv.reader(f)       # skip header
    for row in rows:           # loop over lines
        if len(row):           # check if not an empty line
            prices[row[0]] = float(row[1])

    return prices


def make_report(portfolio, prices):
    """creates report data as a list of tuples

    Args:
        portfolio (list): a list of dictionaries of the stocks
        prices (dict): a dictionary of current stock prices
    
    Returns:
        list: a list of tuples containing report data
    """
    report = []
    for stock in portfolio:
        # stock info: name, #shares, current price, change in price
        stock_info = ( 
            stock['name'], 
            stock['shares'],
            prices[stock['name']],
            prices[stock['name']] - stock['price']
        )
        report.append(stock_info)
    return report


def print_report(report):
    """takes the list of lines info to print and prints them

    Args:
        report (list): a list containing the lines to print
    """
# print header and dashes
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(' '.join([f'{header:>10s}' for header in headers]))
    print(' '.join(['-'*10 for header in headers])) # or using f'{"":->10s}'

    # print the report data
    for name, shares, price, change in report:
        # using nested formmated strings f'{ f"{}" }'
        print(f'{name:>10s} {shares:>10d} {f"${price:>0.2f}":>10s} {change:>10.2f}')


# grab the filename from terminal
filename = sys.argv[1] if len(sys.argv) == 2 else 'Data/portfolio.csv'

# read the portfolio and the prices
portfolio = read_portfolio(filename)
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)    # print the report
