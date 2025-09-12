import pandas as pd

# Specifying the file location (Make sure to provide the file path of your own excel file)
file_path = 'your-file.xlsx'

# Reading the excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Print out the dataframe to verify results
print(df)
