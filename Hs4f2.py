from itertools import permutations
n=str(input())
perms = [''.join(p) for p in permutations(n)]
f=[]
for i in perms:
    if i not in f:
        f.append(i)
print(*f,sep="\n")



