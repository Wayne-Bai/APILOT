# Import necessary libraries
import numpy as np

# Load data from a text file
def load_data(file_path):
    try:
        # Use numpy.loadtxt to load the data from the file
        data = np.loadtxt(file_path)
        
        # Replace missing values with NaN
        # Assuming missing values are represented as "NaN" or a specific numerical value
        data = np.where(data!= data, np.nan, data)
        
        return data
    
    except FileNotFoundError:
        print("The file does not exist")
        return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None

# Example usage:
file_path = 'data.txt'  # specify your file path here
data = load_data(file_path)

if data is not None:
    print("Data loaded successfully: ")
    print(data)
