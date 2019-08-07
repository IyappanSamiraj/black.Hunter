n=int(input())
a=list(map(int,input().split()))
for i in range(n):
	for j in range(n):
		for k in range(n):
			if(i<j<k):
			    if(a[i]+a[j]==a[k]):
			    	print(a[i],a[j],a[k])
