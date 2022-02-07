def simpleSieve(limit):
    mark = [True for i in range(limit)]
    p=2
    for p in range(p*p,limit-1,1):

        if (mark[p]==True):
            for i in range(p*p,limit-1,p):
                mark[i]=False
    for p in range(2,limit-1,1):
        if(mark[p]==True):
            print(p,end=" ")

simpleSieve(100)