import sys
sys.path.append('../Utils')
import ioutils
import numpy as np
import business

file = sys.argv[1]
arr = ioutils.read_array2d(file)
print('Input was')
print(np.matrix(arr))
business.mirror(arr)
print('Out was')
print(np.matrix(arr))
