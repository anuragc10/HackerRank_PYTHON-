n=int(input())


for i in range(n):
    a=input()
    if((a[0]=='7' or a[0]=='8' or a[0]=='9')):
        if(len(a)==10 and (a.isdigit())):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
