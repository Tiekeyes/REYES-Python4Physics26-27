import numpy as np

#2-dimensional array
array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [12, 14, 15, 16]])

# array[start: ending (exclusive indexing): step]
print(array[::-1])

# select all rows, then select the first element in each row
# effectively selecting the 1st column
print(array[:, 0])

# last 3 columns
print(array[:, 1:4])

# every 2nd coumns starting at the 2nd column
print(array[:, 1::2])

# row and column selection 
# first 2 rows, last 2 columns (2:4)
print(array[0:2, 2:])

