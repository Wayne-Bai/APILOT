import numpy as np

# Function to load data from a text file and handle missing values
def load_data(filename, missing_value=None):
    data = np.loadtxt(filename, delimiter=',', dtype=str)

    # Replace missing values if specified
    if missing_value is not None:
        data = np.where(data == missing_value, '', data)

    # Convert string data to appropriate type
    try:
        data = np.array(data, dtype=float)
    except ValueError:
        print("Could not convert all data to floating point. Please check your input file.")
        return

    return data

# Usage example
filename = 'data.txt'
missing_value = 'NaN'  # Replace with actual placeholder for missing values
data = load_data(filename, missing_value)

if data is not None:
    print(data)
