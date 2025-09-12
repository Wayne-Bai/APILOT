# Import the pandas library
import pandas as pd

# Read an Excel file into a pandas DataFrame
def read_excel_file(file_path, sheet_name=None):
    try:
        # Check if a sheet name is provided
        if sheet_name:
            # Read a specific sheet from the Excel file
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            # Read the first sheet from the Excel file
            df = pd.read_excel(file_path)
        
        # Return the DataFrame
        return df
    
    except Exception as e:
        print(f"Failed to read the Excel file: {str(e)}")
        return None

# Example usage
file_path = "example.xlsx"
sheet_name = "Sheet1"

df = read_excel_file(file_path, sheet_name)

# Check if the DataFrame is not None
if df is not None:
    # Print the first few rows of the DataFrame
    print(df.head())
