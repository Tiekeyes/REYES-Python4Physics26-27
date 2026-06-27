import numpy as np

#1 row, 4 columns
array1 = np.array([[1, 2, 3, 4]])
#4 rows, 1 column
array2 = np.array([[1], [2], [3], [4]])

print(array1 * array2)

#broadcasting only works if:
# 1. two arrays have the same column/row
# 2. the other dimension is equal to 1 for one of the arrays
#       or
# 1. two arrays have the same shape