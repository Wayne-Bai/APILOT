import pandas as pd

# Specify the file path of the Excel file you want to read
file_path = 'your_file.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())
