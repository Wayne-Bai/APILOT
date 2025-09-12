import numpy as np

def load_data_from_text_file(file_path):
    """
    Load data from a text file.

    Parameters:
    file_path (str): The path to the text file.

    Returns:
    numpy.ndarray: A 1D or 2D array containing the data from the text file.
    """

    try:
        # Attempt to load the data from the text file
        data = np.loadtxt(file_path)

        return data

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None

    except ValueError:
        print(f"Unable to parse the file {file_path}.")
        return None


# Example usage:
file_path = "data.txt"  # Replace with your own file path
loaded_data = load_data_from_text_file(file_path)

if loaded_data is not None:
    print("Loaded Data:")
    print(loaded_data)
