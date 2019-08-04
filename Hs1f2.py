n=str(input())
words=n.split(" ")
new=[word[::-1] for word in words]
sent=" ".join(new)
print(sent)
