import numpy as np

# Assuming we have a 1D array for simplicity
np.random.seed(0)  # For reproducibility
data = np.random.rand(100)

# Compoute 25 percentile by default (q=0.25)
q = 0.25

# Using np.percentile function, q represents the percentile and axis=0 means we compute along the first axes (default if not specified)
np.percentile(data, q*100)
