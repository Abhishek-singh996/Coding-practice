def palindrom(s):
    s1 = s[::-1]
    return s1
s = input("enter the string: ")
print(s)
q = palindrom(s)
print(q)
if q == s:
    print("yes")
else:
    print("no")