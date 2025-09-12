# Import necessary libraries
import numpy as np

# Load data from a text file
def load_data(file_path):
    try:
        data = np.loadtxt(file_path)
        return data
    except ValueError as e:
        print(f"Error loading data: {e}")
        return None

# Handle missing values (assumed to be NaN in NumPy)
def handle_missing_values(data):
    # Replace missing values with the mean of the respective column
    data = np.nan_to_num(data, nan=np.nanmean)
    return data

# Main function
def main():
    file_path = 'data.txt'  # replace with your text file path
    data = load_data(file_path)
    
    if data is not None:
        print("Loaded data:")
        print(data)
        
        data_with_missing_values_handled = handle_missing_values(data)
        print("\nData with missing values handled:")
        print(data_with_missing_values_handled)

if __name__ == "__main__":
    main()
