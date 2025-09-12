import pandas as pd

# Read an Excel file into a pandas DataFrame
file_path = 'your_file.xlsx'  # Replace with your Excel file path
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())
