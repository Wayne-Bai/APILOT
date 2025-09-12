import numpy as np
from scipy.stats import variation

# Sample data
data = [10, 20, 30, 40, 50]

# Compute the coefficient of variation
coef_variation = variation(data)

print("Coefficient of Variation:", coef_variation)
