def Repeat(x): 
    size = len(x) 
    repeated = [] 
    for i in range(size):         
         if x[i] is i : 
              repeated.append(i) 
    return repeated   
Num=int(input())
list1=list(map(int,input().split()))
n=sorted(Repeat(list1))
if len(n)!=0:
    print(*n)
else:
    print('-1')
