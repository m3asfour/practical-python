# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    extra_payment = 1000 if months < 12 else 0
    principal = principal * (1 + rate/12) - (payment + extra_payment)
    total_paid += payment + extra_payment
    months += 1

print(f'Total Paid: {total_paid:0.2f}. It took {months} months.')
