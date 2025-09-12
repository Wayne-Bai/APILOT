
import numpy as np

def coefficient_of_variation(data):
    mean_value = np.mean(data)
    std_deviation = np.std(data)
    
    coefficient_var = std_deviation / mean_value
    
    return coefficient_var

# Example of how to use the function
data = [32, 56, 12, 87, 45, 67, 23]
cv_result = coefficient_of_variation(data)
print("Coefficient of Variation:", cv_result)
