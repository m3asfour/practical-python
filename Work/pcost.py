# pcost.py
#
# Exercise 1.27

line_num = 0
all_shares_price = 0

with open('Data/portfolio.csv', 'rt') as f:
    for line in f:
        line_num += 1
        if line_num == 1:
            continue

        stock_name, shares_num, stock_price = line.strip().split(',')
        all_shares_price += int(shares_num) * float(stock_price)

print(f'Total cost {all_shares_price}')
