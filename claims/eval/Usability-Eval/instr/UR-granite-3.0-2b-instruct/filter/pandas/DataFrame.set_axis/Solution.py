import pandas as pd

# Create a sample dataframe
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# Assign a desired index to the given axis
df.set_index('Name', inplace=True)

# Print the dataframe
print(df)
