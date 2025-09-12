import pandas as pd

# Let's create a simple DataFrame to write to an Excel file
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 33]}
df = pd.DataFrame(data)

# Writing to an Excel file 'my_data.xlsx'
df.to_csv('my_data.xlsx', index=False)
