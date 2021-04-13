n,m=map(int,input().split())
l=[0]*n

for _ in range(m):
    a,b,k=map(int,input().split())
    i=0
    for i in range(n):
        if(i>=(a-1) and i<b):
            l[i]=l[i]+k
        else:
            continue
print(max(l))
