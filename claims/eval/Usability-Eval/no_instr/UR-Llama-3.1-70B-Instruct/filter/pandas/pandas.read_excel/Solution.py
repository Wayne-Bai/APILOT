# Import the pandas library
import pandas as pd

# Function to read an Excel file into a pandas DataFrame
def read_excel_file(file_path):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)
        
        # Return the DataFrame
        return df
    
    except FileNotFoundError:
        print("The file does not exist")
        return None
    
    except Exception as e:
        print("An error occurred: ", e)
        return None

# Example usage
file_path = "example.xlsx"  # Replace with your Excel file path
df = read_excel_file(file_path)

# Print the first few rows of the DataFrame
if df is not None:
    print(df.head())
