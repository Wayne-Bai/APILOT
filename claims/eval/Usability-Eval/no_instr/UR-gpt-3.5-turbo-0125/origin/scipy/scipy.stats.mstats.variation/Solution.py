
import numpy as np

# Define a function to calculate the coefficient of variation
def coefficient_of_variation(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    coefficient_var = (std_dev / mean) * 100
    return coefficient_var

# Test the function with sample data
data = np.array([4, 7, 9, 13, 16])
result = coefficient_of_variation(data)
print("Coefficient of Variation:", result)
