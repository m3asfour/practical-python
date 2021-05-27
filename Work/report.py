# report.py
#
# Exercise 2.10


import csv

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
            holding = {
                'name'  : row[0], 
                'shares': int(row[1]),
                'price' : float(row[2])}

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


# read the portfolio and the prices
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

# print the report data
for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
