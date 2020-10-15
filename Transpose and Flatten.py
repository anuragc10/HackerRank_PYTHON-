import numpy as np

N,M=(map(int,input().split()))

l2=list()
for i in range(N):
    l=list(map(int,input().split()))
    l2.append(l)

arr=np.array(l2)
print(np.transpose(arr))
print(arr.flatten())

