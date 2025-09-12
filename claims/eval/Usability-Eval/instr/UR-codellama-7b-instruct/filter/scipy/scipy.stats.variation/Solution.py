
from scipy import stats
import numpy as np

# Compute the coefficient of variation for two arrays of data
def coef_var(x, y):
    # Compute the mean and variance of each array
    mu_x = x.mean()
    var_x = x.var()
    mu_y = y.mean()
    var_y = y.var()
    
    # Compute the coefficient of variation for each array
    cv_x = np.sqrt(var_x / (mu_x ** 2))
    cv_y = np.sqrt(var_y / (mu_y ** 2))
    
    # Return the coefficient of variation as a tuple
    return (cv_x, cv_y)
