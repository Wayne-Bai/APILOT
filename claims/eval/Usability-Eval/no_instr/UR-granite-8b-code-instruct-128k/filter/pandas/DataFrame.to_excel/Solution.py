import pandas as pd

# Create a sample object
data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel sheet
df.to_excel('sample.xlsx', index=False)
