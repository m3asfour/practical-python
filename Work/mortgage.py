# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    current_month += 1

    if current_month >= extra_payment_start_month and current_month <= extra_payment_end_month:
        month_extra_payment = extra_payment
    else:
        month_extra_payment = 0

    principal = principal * (1 + rate/12) - (payment + month_extra_payment)
    total_paid += payment + month_extra_payment

    if principal < 0:
        total_paid -= -principal
        principal += -principal
    
    print(f'>> {current_month:<4}  |  {total_paid:^12.2f}|  {principal:^12.2f}')

print(f'Total Paid {total_paid:0.2f}\nMonths {current_month}')