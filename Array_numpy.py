import numpy

def arrays(arr):
    arr1=numpy.array(arr,float)[::-1]
    return arr1

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
