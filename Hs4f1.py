def findSingle( ar, n): 
    res = ar[0] 
    for i in range(1,n): 
        res = res ^ ar[i] 
    return res
n=int(input())
ar = list(map(int,input().split()))
print (findSingle(ar, len(ar)) )

  
