import pandas as pd

# Define the path to the Excel file
file_path = 'path/to/your/excel/file.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Display the first 5 rows of the DataFrame
print(df.head())
