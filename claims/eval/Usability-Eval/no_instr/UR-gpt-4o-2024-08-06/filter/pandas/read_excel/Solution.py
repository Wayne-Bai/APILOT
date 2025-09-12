import pandas as pd

# Read the Excel file into a DataFrame
excel_file_path = 'your_file_path.xlsx'  # Replace with your file path
df = pd.read_excel(excel_file_path)

# Display the first few rows of the DataFrame
print(df.head())
