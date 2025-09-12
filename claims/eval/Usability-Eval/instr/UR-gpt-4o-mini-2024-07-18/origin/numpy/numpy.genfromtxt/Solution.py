import numpy as np

# Function to load data from a text file and handle missing values
def load_data_with_nan(filepath, missing_value='nan'):
    # Load data using numpy's loadtxt with the option to replace missing values
    data = np.loadtxt(filepath, delimiter=',', dtype=float, 
                       missing_values=missing_value, 
                       filling_values=np.nan)
    return data

# Example usage
# data = load_data_with_nan('data.txt')
