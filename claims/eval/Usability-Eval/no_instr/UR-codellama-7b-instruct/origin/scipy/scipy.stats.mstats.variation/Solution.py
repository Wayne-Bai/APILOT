
import numpy as np
from scipy.stats import variation

# Function to compute the coefficient of variation
def coefficient_of_variation(data):
    # Calculate the sample variance
    sample_variance = variation(data, ddof=1)
    
    # Calculate the population standard deviation
    stddev = np.std(data, ddof=1)
    
    # Calculate the coefficient of variation
    cv = (sample_variance / stddev) * 100
    
    return cv
