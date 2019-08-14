from itertools import permutations
n=str(input())
perms = [''.join(p) for p in permutations(n)]
print(*perms,sep="\n")
