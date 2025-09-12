# Importing the necessary library
import numpy as np

def load_data(filename, missing_values, dtype):
    # Use numpy's genfromtxt function with proper parameters to handle missing values
    data = np.genfromtxt(filename, dtype=dtype, missing_values=missing_values, filling_values=0)
    return data
