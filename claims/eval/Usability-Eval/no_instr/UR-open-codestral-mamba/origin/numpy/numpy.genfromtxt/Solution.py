import numpy as np

def load_data(filename, missing_value):
    """
    Load data from a text file, replacing missing values according to the specified handling method.

    Parameters:
    filename (str): The path to the text file to be loaded.
    missing_value (float): The value to be treated as missing, which will be replaced based on the specified method.

    Returns:
    numpy.ndarray: The loaded data array with missing values replaced according to the specified method.
    """
    # Load data from the text file using numpy's genfromtxt function
    data = np.genfromtxt(filename, delimiter=',', missing_values=missing_value, dtype=np.float)

    # Check if any of the loaded data contains the missing value
    has_missing_value = np.isnan(data).any()

    if has_missing_value:
        print(f"Missing value {missing_value} found in the data.")
    else:
        print("No missing values found in the data.")

    # Replace missing values with the specified handling method
    # For example, here we replace missing values with the mean of the column/row
    mean_values = np.nanmean(data, axis=0)

    for column in data:
        missing_indices = np.isnan(column)
        column[missing_indices] = mean_values[np.where(column == missing_value)[0]]

    return data
