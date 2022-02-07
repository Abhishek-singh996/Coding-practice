
def sumOfDigits(n):
    sum  = 0
    while n>0:
        sum = sum + int(n%10)
        n = n/10
    return sum
n = 651
print(sumOfDigits(n))