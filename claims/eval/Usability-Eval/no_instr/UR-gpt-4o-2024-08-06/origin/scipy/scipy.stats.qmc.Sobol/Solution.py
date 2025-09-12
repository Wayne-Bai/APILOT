import numpy as np
from scipy.stats.qmc import Sobol

# Initialize the Sobol sequence generator
# In this example, the dimension size is set to 2, you can set it to the required dimension
dimension = 2
sobol = Sobol(d=dimension, scramble=True)

# Generate a scrambled Sobol sequence
# You can specify how many points you need
num_points = 10
sequence = sobol.random(n=num_points)

print("Scrambled Sobol sequence:")
print(sequence)
