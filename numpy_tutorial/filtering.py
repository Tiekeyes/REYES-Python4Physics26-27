import numpy as np

ages = np.array([np.random.randint(18, 40, 10), np.random.randint(18, 40, 10)])
print(ages)

#find anyone who is under 21
#returns a single-row array
under_21 = ages[ages < 21]
print(under_21)

#find anyone who is between 30~35
#use & instead of and
#use | instead of or
old = ages[(ages >= 30) & (ages <=35)]
print(old)

adults = np.where(ages > 18, ages, 0)
print(adults)