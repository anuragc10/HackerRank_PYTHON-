import numpy as np
np.set_printoptions(sign=' ')
L=list(map(float,input().split()))
arr=np.array(L)

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
