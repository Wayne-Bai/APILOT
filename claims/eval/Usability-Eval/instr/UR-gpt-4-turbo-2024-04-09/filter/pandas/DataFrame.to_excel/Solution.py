import pandas as pd

# Create a sample dataframe
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 22, 34, 40],
        'City': ['New York', 'Paris', 'Berlin', 'London']}

df = pd.DataFrame(data)

# Write the dataframe to an Excel file
df.to_excel('output.xlsx', index=False)
