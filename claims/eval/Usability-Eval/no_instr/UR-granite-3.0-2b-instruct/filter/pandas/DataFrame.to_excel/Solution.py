import pandas as pd

# Create a simple dataframe
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Write the dataframe to an Excel file
df.to_excel('output.xlsx', index=False)
