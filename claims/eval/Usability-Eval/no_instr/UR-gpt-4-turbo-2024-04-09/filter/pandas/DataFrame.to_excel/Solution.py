import pandas as pd

# Creating a sample dataframe
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 22, 34, 42],
        'City': ['New York', 'Paris', 'Berlin', 'London']}

df = pd.DataFrame(data)

# Writing the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
