import pandas as pd

# Create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Male']}
df = pd.DataFrame(data)

# Hide specific columns from rendering
df = df[['Name', 'Gender']]

# Render the dataframe without headers
print(df.to_string(header=False))
