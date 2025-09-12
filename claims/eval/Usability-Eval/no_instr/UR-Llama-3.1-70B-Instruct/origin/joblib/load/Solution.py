# Import the joblib library
import joblib

# Function to load the Python object from a file
def load_object(file_path):
    """
    Reconstruct a Python object from a file persisted with joblib.dump.

    Args:
    file_path (str): Path to the file containing the dumped object.

    Returns:
    object: The loaded Python object.
    """
    try:
        # Load the object from the file
        loaded_object = joblib.load(file_path)
        return loaded_object
    except FileNotFoundError:
        print(f"File not found at the specified path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = "path_to_your_file.pkl"  # Replace with your file path
    loaded_object = load_object(file_path)
    print(loaded_object)
