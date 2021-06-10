n,m=map(int,input().split())
l=list(map(int,input().split()))
q=n-m
for i in range(q):
    t=l[n-1]
    del l[-1]
    l.insert(0,t)
print(*l)
