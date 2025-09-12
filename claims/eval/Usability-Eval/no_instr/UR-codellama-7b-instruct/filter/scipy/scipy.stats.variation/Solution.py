import numpy as np
from scipy import stats

# Compute the coefficient of variation
def compute_coefficient_of_variation(data):
    # Calculate the mean and standard deviation of the data
    mean = np.mean(data)
    stddev = np.std(data, ddof=1)
    
    # Calculate the coefficient of variation
    cv = stddev / mean * 100
    
    return cv
