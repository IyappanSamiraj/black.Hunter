def Repeat(x): 
    size = len(x)  
    repeated=[]
    for i in range(size): 
        k = i + 1
        for j in range(k, size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated   
Num=int(input())
list1=list(map(int,input().split()))
n=Repeat(list1)
if len(n)!=0:
    print(n[0])
else:
    print('unique')
