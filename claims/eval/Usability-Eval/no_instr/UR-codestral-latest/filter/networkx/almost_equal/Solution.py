import numpy as np

def compare_numbers(num1, num2, tolerance):
    return np.allclose(num1, num2, atol=tolerance)
