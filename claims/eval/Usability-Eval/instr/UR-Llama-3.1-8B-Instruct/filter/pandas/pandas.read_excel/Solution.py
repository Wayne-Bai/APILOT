# Import the pandas library
import pandas as pd

# Function to read the Excel file
def read_excel_file(file_location):
    try:
        # Read the Excel file into a pandas DataFrame using the read_excel function (pandas.read_excel())
        # pandas.read_excel() has been updated and has alias, use read_excel from the top-level pd module that can handle both xlsx and xls
        df = pd.read_excel(file_location)
        return df
    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty. Please check the file.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file. Please check the file format.")
        return None

# Example usage
filename = 'example.xlsx'  # replace with your Excel file location
df = read_excel_file(filename)
if df is not None:
    print(df.head())  # print the first 5 rows of the DataFrame
    print(df.info())  # print information about the DataFrame
