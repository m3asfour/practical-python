# bounce.py
#
# Exercise 1.5

# initial height and number of bounces
height = 100
bounces = 10

for bounce in range(bounces):
    height *= 3/5           # update the height
    print(bounce+1, height) # bounce starts from 0