import scipy.stats
import numpy as np

def coefficient_of_variation(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    cv = std_dev / mean
    return cv

data = [5, 10, 15, 20, 25]
cv = coefficient_of_variation(data)
print("Coefficient of Variation:", cv)
