# report.py
#
# Exercise 2.5


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
                'name': row[0], 
                'shares': int(row[1]),
                'price': float(row[2])}
                
            portfolio.append(holding)

    return portfolio    