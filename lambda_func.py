"""lambda arguments : expression"""

sum_digit = lambda n: sum([int(x) for x in str(n)])
print(sum_digit(1023))