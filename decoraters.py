import time 
import math

def func1(func):
    def inner1(*args,**kwargs):
        begin = time.time()
        x = func(*args,**kwargs)
        end = time.time()
        print(f'Total time taken for the {func.__name__} : {end-begin}')

        return x
    return inner1

@func1
def sum_number(num1,num2):
    time.sleep(2)
    return num1+num2

@func1
def diff_number(num1,num2):
    time.sleep(2)
    return num1-num2

print(sum_number(4,5))
print(diff_number(4,5))