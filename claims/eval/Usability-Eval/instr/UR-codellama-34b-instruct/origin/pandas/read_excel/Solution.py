import pandas as pd

# Read the Excel file using the latest API (pd.read_excel) and save it as a variable "df"
df = pd.read_excel("your_file.xlsx")

# View the first few rows of the DataFrame
print(df.head())
