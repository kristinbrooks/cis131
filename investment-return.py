"""
    7% Investment Return

    Some investment advisors say that it’s reasonable to expect a 7% return over the long term in the stock market. If you
    begin with $1000 and leave your money invested, calculate, and display how much money you’ll have after 10, 20 and 30
    years. Use the following formula for determining these amounts:

    a = p(1 + r)n
    where
    p is the original amount invested (i.e., the principal of $1000),
    r is the annual rate of return (7%),
    n is the number of years (10, 20 or 30) and
    a is the amount on deposit at the end of the
    nth year.
"""

# set constants
p = 1000
r = 0.07

# calculate amount after 10 years
n = 10
a = p * (1 +r) ** n

# print 10 year result
print(f'After 10 years the original $1000 dollars will grow to ${a:.2f}')

# calculate amount after 20 years
n = 20
a = p * (1 +r) ** n

# print 20 year result
print(f'After 20 years the original $1000 dollars will grow to ${a:.2f}')

# calculate amount after 30 years
n = 30
a = p * (1 +r) ** n

# print 30 year result
print(f'After 30 years the original $1000 dollars will grow to ${a:.2f}')
