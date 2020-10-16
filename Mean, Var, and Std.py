import numpy as np

np.set_printoptions(legacy='1.13')
N,M=map(int,input().split())
A = np.array([ input().split() for i in range(N) ],int)

print (np.mean(A, axis = 1))
print (np.var(A, axis = 0))
print (np.std(A))
