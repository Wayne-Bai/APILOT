import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
excel_file_path = 'sample_data.xlsx'
df.to_excel(excel_file_path, index=False, sheet_name='Sheet1')

print(f"DataFrame has been written to {excel_file_path}")
