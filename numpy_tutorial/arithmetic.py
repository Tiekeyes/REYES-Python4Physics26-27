import numpy as np

#Scalar Arithmetic
array = np.array([1, 2, 3])

#add one to each element
array += 1

#raise each element to the power of 5
array = array**5


#Vectorized Arithmetic
radii = np.array([1, 2, 3, 4])

#square, then round each value
print(np.round(np.sqrt(radii)))

#calculating the area of each radius
areas = np.round(np.pi * radii ** 2)
print(areas)


#Element-wise Arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)


#Comparison Operators
scores = np.array([91, 55, 100, 73, 82, 64])

#find the student who got a perfect score
print(scores == 100)

#find students who scored more than 60
print(scores > 60)

#re-assigns any student who got less than 60 a fail (0)
scores[scores < 60] = 0
print(scores)