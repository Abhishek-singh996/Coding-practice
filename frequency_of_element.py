def countfreq(arr,n):
    mp = dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for x  in mp:
        print(f"{x}  {mp[x]}")
arr = [10,20,20,10,30]
q = countfreq(arr,n=len(arr))

