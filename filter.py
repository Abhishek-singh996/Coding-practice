a = list((1,2,3,4,5,6,7,8,9,10))

def filter_num(x):
    if x>5:
        return False
    else:
        return True
    
y = filter(filter_num,a)
for i in y:
    print(i)