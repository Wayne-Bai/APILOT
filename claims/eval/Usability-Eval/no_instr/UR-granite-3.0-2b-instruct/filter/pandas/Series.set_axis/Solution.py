import pandas as pd

# Create a sample dataframe
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 24, 35],
        'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# Set the 'Name' column as the index
df.set_index('Name', inplace=True)

# Print the dataframe with the desired index
print(df)
