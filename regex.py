import re
x = re.split('[A-Za-z]','abhi12sin345dfg5')
sum=0
for i in x:
    if i.isnumeric():
        sum+=int(i)
print(sum)
