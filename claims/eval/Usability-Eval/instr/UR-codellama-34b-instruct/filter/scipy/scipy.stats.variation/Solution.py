
from scipy import stats
import numpy as np

# Generate some sample data
data = np.random.normal(size=10)

# Compute the coefficient of variation using the `variation` function
cv = stats.variation(data)

print("Coefficient of variation:", cv)
