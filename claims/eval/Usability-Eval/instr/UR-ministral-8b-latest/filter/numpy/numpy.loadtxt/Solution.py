import numpy as np

def load_data_from_file(filename):
    """
    Load data from a text file where each line contains a number.

    :param filename: Path to the text file.
    :return: numpy array of the data.
    """
    try:
        data = np.loadtxt(filename)
        return data
    except Exception as e:
        print(f"Error loading data from file: {e}")
        return np.array([])

# Example usage:
filename = 'data.txt'
data = load_data_from_file(filename)
print(data)
