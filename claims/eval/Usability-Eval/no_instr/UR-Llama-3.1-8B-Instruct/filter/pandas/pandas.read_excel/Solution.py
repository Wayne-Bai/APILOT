# Import the pandas library
import pandas as pd

# Read the Excel file into a pandas DataFrame
def read_excel_file(file_path, sheet_name='Sheet1'):
    try:
        # Use the pd.read_excel function to read the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("The Excel file is empty.")
        return None

# Example usage:
file_path = 'example.xlsx'
df = read_excel_file(file_path)
if df is not None:
    print(df.head())  # Print the first few rows of the DataFrame
