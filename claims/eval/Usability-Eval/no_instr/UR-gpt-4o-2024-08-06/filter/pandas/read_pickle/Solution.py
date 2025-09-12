import pandas as pd

# Load a pickled pandas DataFrame
def load_pickled_object(file_path):
    # Use pd.read_pickle to load the DataFrame from a pickle file
    try:
        data = pd.read_pickle(file_path)
        return data
    except (FileNotFoundError, IOError) as e:
        print(f"Error loading file: {e}")
        return None

# Example usage
file_path = 'data.pkl'  # Replace with your actual file path
loaded_data = load_pickled_object(file_path)

if loaded_data is not None:
    print("Data loaded successfully:")
    print(loaded_data)
else:
    print("Failed to load data.")
