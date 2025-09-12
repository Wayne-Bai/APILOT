
import numpy as np

def coefficient_of_variation(data):
    mean = np.mean(data)
    std = np.std(data)
    
    if mean == 0:
        coefficient_variation = np.inf
    else:
        coefficient_variation = std / mean
    
    return coefficient_variation

# Example usage:
data = [10, 20, 30, 40, 50]
result = coefficient_of_variation(data)
print("Coefficient of variation:", result)
