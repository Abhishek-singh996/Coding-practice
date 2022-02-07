# m = [[1,2, 3],
#     [2,3,4],
#     [3,4,5]]
# m1= [[1,2, 3],
#     [2,3,4],
#     [3,4,5]]
# m2=[[0,0,0],
#     [0,0,0],
#     [0,0,0]]
# for i in range(len(m)):
#     for j in range(len(m1[0])):
#         for k in range(len(m1)):
#             m2[i][j]+=m[i][k]*m1[k][j]
# for i in m2:
#     print(i)
import numpy as np
m = [[1,2, 3],
    [2,3,4],
    [3,4,5]]
m1= [[1,2, 3],
    [2,3,4],
    [3,4,5]]
q=np.dot(m,m1)
print(q)
