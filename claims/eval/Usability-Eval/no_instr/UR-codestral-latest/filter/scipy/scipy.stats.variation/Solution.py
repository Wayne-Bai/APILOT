import numpy as np
from scipy.stats import variation

# Let's assume we have some data
data = np.array([1, 2, 3, 4, 5])

# Compute the coefficient of variation
coef_var = variation(data)

print(f'The coefficient of variation is: {coef_var}')
