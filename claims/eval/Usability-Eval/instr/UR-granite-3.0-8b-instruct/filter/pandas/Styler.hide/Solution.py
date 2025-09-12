import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 24, 35],
        'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# Hide the entire index
df.index.name = None

# Hide specific columns
df = df.drop(['Name', 'City'], axis=1)

# Hide specific rows
df = df.drop([0], axis=0)

# Display the DataFrame without index, column headers, or specific rows/columns
print(df)
