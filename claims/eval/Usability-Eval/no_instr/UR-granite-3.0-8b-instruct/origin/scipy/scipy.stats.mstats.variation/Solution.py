import numpy as np
from scipy.stats import variation

# Assuming you have a list of numbers
data = [1, 2, 3, 4, 5]

# Compute the mean
mean = np.mean(data)

# Compute the standard deviation
std_dev = np.std(data)

# Compute the coefficient of variation
coeff_var = std_dev / mean

print(f"The coefficient of variation is: {coeff_var}")
