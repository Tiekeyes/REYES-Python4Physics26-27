import numpy as np

#1 dimensional arrays
array = np.array(['A'])
array_1 = np.array(['A', 'B', 'C'])

#2 dimensional arrays
array_2 = np.array([['A', 'B', 'C'], 
                    ['B', 'A', 'C']])

#3 dimensional arrays
array_3 = np.array([[['A', 'B', 'C'], ['A', 'B', 'C']], 
                    [['B', 'C', 'A'], ['A', 'B', 'C']]])


#ndim = number of dimensions
print(array_1.ndim, array_2.ndim, array_3.ndim)

#prints the shape of array 
print(array_1.shape, array_2.shape, array_3.shape)

#prints the element in the 2nd row, 1st column, 2nd element
print(array_3[1, 0, 1])

