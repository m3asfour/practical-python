# report.py
#
# Exercise 3.18


import sys
import os
import fileparse

def read_portfolio(filename):
    """parses a csv file into a list of tuples

    Args:
        filename (str): the path of the csv file

    Returns:
        list: list of dictionaries. each tuple contains info of one line
    """
    # use the fileparse module
    portfolio = fileparse.parse_csv(filename, 
                                    select=['name', 'shares','price'],
                                    types=[str, int, float])
    return portfolio    


def read_prices(filename):
    """reads the stock prices from the csv file

    Args:
        filename (str): file path of the prices csv file

    Returns:
        dict: a dictionary of prices by stock name
    """
    # use the fileparse module
    prices = fileparse.parse_csv(filename, types=[str, float], has_headers=False)
    prices = dict(prices)   # convert into a dictionary
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
        print(f'{name:>10} {shares:>10} {f"${price:>0.2f}":>10} {change:>10.2f}')


def portfolio_report(portfolio_file, prices_file):
    """parses the portfolio, computes the report's values, and prints it

    Args:
        portfolio_file (str): filepath of the portfolio csv file
        prices_file ([type]): filepath of the prices csv file
    """
    # grab the filename from terminal if provided
    filename = sys.argv[1] if len(sys.argv) == 2 else portfolio_file

    # read the portfolio and the prices
    portfolio = read_portfolio(filename)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)    # print the report


def main(cmd_lines):
    os.system(f'python ' + ' '.join(cmd_lines))


# check if filepaths were passed to generate a report and that the script is executed (not imported)
if len(sys.argv) > 1 and sys.argv[0] == 'report.py':
    portfolio_csv = sys.argv[1]
    prices_csv = sys.argv[2] if len(sys.argv) == 3 else 'Data/prices.csv'
    portfolio_report(portfolio_csv, prices_csv)
