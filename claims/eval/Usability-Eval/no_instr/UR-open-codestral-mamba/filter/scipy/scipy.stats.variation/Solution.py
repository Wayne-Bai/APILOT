import numpy as np
from scipy import stats

# Assuming data is a numpy array containing the data

def compute_coef_var(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    coef_var = std_dev / mean
    return coef_var

data = np.array([1, 2, 3, 4, 5])  # Test data
print(compute_coef_var(data))
