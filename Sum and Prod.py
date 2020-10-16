#python 2 code

import numpy as np

N, M = map(int, raw_input().split())
arr = np.array([ map(int, raw_input().split()) for i in range(N) ])
print np.prod( np.sum( arr, axis = 0 ) )
