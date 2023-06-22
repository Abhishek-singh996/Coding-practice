a = (1,2,3,4,5,6)
b = (1,2,3,4,5,6)

z = tuple((x,y) for x in a for y in b if (x+y)>11)

print(z)
    
