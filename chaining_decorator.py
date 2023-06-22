def func1(func):
    def inner():
        x = func()*func()
        return x
    return inner
    
def func2(func):
    def inner():
        x = 2*func()
        return x
    return inner
    
@func1
@func2
def num1():
    return 10

@func2
@func1
def num2():
    return 20

print(num1())
print(num2())
