import numpy as np
from scipy.stats import variation

# Assuming you have a data array
data = np.array([10, 15, 20, 25, 30])

# Compute the coefficient of variation
coefficient_of_variation = variation(data)

print("The coefficient of variation is:", coefficient_of_variation)
