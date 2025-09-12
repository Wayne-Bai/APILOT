import numpy as np

# Define two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Define a function to evaluate Einstein summation convention
def einstein_summation(a, b):
    # Create a new array with the same shape as a and b
    result = np.zeros_like(a)

    # Iterate over the arrays
    for i in range(len(a)):
        # Calculate the sum of the corresponding elements
        result[i] = np.sum(a * b)

    return result

# Call the function and print the result
print(einstein_summation(a, b))
