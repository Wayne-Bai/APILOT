# Import the pandas library
import pandas as pd

# Read an Excel file into a pandas DataFrame
def read_excel_file(file_path):
    """
    Reads an Excel file into a pandas DataFrame.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the Excel file data.
    """
    try:
        # Use pandas read_excel function with engine='openpyxl'
        df = pd.read_excel(file_path, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")
        return None

# Example usage
file_path = 'example.xlsx'
df = read_excel_file(file_path)

if df is not None:
    # Print the first few rows of the DataFrame
    print(df.head())
    # Print the info of the DataFrame
    print(df.info())
