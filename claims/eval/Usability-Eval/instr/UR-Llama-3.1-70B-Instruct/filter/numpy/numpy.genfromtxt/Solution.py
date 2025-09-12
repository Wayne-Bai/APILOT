import numpy as np

def load_data_from_file(file_path, missing_values=np.nan, delimiter=None):
    """
    Load data from a text file, with missing values handled as specified.

    Parameters:
    file_path (str): Path to the text file.
    missing_values (str or int or float): Value to recognize as missing or None for the default.
    delimiter (str): Character used to separate values.

    Returns:
    ndarray: A 2D array of the data loaded from the file.
    """
    try:
        data = np.loadtxt(file_path, delimiter=delimiter)
        # Replace missing values with NaN if specified
        if missing_values is not None:
            data[data == missing_values] = np.nan
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except ValueError as e:
        print("Error parsing the file: ", str(e))
        return None


# Usage
file_path = 'data.txt'
data = load_data_from_file(file_path, missing_values='NA', delimiter=',')
print(data)
