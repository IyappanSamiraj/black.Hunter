num=int(input())
n=list(map(int,input().split()))
s=sorted(n,reverse=True)
print(sep='',*s)
