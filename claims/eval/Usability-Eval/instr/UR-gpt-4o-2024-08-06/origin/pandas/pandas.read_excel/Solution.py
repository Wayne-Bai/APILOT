import pandas as pd

# Specify the file path to the Excel file
file_path = 'your_excel_file.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, engine='openpyxl')  # Using openpyxl as the engine

# Display the DataFrame
print(df)
