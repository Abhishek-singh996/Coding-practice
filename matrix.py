m = [[1,2, 3],
    [2,3,4],
    [3,4,5]]
m1= [[1,2, 3],
    [2,3,4],
    [3,4,5]]
m2=[[0,0,0],
    [0,0,0],
    [0,0,0]]


for i in range(len(m)):
    for j in range(len(m)):

        m2[i][j]=m[i][j]+m1[i][j]

for i in m2:
    print(i)
