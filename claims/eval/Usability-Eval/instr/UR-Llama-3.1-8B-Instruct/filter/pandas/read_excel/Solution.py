# Import the pandas library
import pandas as pd

# Read an Excel file into a pandas DataFrame
def read_excel_file(file_path):
    try:
        # Use pd.read_excel() function to read the Excel file
        # The file_path should be the path to the Excel file
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {str(e)}")

# Example usage:
file_path = 'path_to_your_excel_file.xlsx'  # Replace with the actual path to the Excel file
df = read_excel_file(file_path)
print(df)
