import numpy as np

def compute_quantile(data, q):
    if not isinstance(data, np.ndarray) or not isinstance(q, (int, float)):
        raise ValueError("Invalid input. data should be a numpy array and q should be a number.")

    if q < 0 or q > 1:
        raise ValueError("Invalid input. q should be between 0 and 1.")

    return np.quantile(data, q)
