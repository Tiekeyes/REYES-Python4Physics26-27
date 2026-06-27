import numpy as np

rng = np.random.default_rng(seed=1)

#generate an array of numbers from 1~6
random_numbers = rng.integers(1, 7, (3, 2))

print(random_numbers)

#each number has an equal chance of being selected
rng = np.random.uniform()
