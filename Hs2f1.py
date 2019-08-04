import numpy
num=int(input())
n=list(map(int,input().split()))    
s=sorted(n,reverse=True)
if s!=n:
    print(sep='',*s)
else:
    print('0')



