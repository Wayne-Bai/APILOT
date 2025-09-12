
import numpy as np
from scipy import stats

# Define the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Compute the coefficient of variation using the "std" function from scipy
cv = stats.variation(y, x=x)

print(cv)
