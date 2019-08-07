n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    if(i%2==0):
        if(a[i]%2!=0):
            print(a[i],end=' ')
    else:
        if(a[i]%2==0):
            print(a[i],end=' ')
            
