def max_and_min1(A):
    A.sort()
    return (A)
A = [12,23,4,5,6,7,8,66,6,6,55]
q = max_and_min1(A)
print(q[-1],q[0])