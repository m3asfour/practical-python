# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(filename):
    line_num = 0
    all_shares_price = 0

    with open(filename, 'rt') as f:
        lines = csv.reader(f)

        for line in lines:
            line_num += 1
            if line_num == 1:
                continue

            stock_name, shares_num, stock_price = line
            try:
                all_shares_price += int(shares_num) * float(stock_price)
            except ValueError:
                # we can raise a warning instead using "raise Warning(msg)"
                print('Missing Field encountered. Skipping the corresponding line.')

    return all_shares_price

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)