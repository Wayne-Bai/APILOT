# Importing the necessary library
from joblib import load

# Define a function to reconstruct the Python object
def reconstruct_object(file_path):
    """
    Reconstructs a Python object from a file persisted with joblib.dump.
    
    Parameters:
    file_path (str): The path to the persisted file.
    
    Returns:
    object: The reconstructed Python object.
    """
    
    # Try to load the object from the file
    try:
        # Use joblib.load to reconstruct the object
        return load(file_path)
    
    # Handle any exceptions that occur during loading
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
if __name__ == "__main__":
    # Specify the file path to the persisted object
    file_path = "path/to/persisted/object.joblib"
    
    # Reconstruct the object from the file
    reconstructed_object = reconstruct_object(file_path)
    
    # Print the type of the reconstructed object
    print(f"Type of the reconstructed object: {type(reconstructed_object)}")
