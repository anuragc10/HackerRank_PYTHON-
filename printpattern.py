n=int(input())
c=n
d=n

l=['hello','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(l[c],end="")
        c=c-1
    c=n
    for p in range(1,i):
        print(l[d],end="")
        d=d+1
    d=n-(i-1)
    print("")

for i in range(1,n):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,n-i+1):
        print(l[c],end="")
        c=c-1
    c=n
    d=i+2
    for p in range(1,n-i):
        print(l[d],end="")
        d=d+1
    print("")
