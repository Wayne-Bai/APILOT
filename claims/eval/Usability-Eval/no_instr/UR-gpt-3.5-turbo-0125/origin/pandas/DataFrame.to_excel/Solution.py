
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
excel_filename = 'output_data.xlsx'
df.to_excel(excel_filename, index=False)
print(f'Data written to {excel_filename} successfully.')
