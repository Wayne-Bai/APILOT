
import numpy as np

def is_within_machine_limits(num):
    # Check if the number is within the range of a float64
    if num >= -np.finfo(np.float64).max and num <= np.finfo(np.float64).max:
        return True
    else:
        return False
