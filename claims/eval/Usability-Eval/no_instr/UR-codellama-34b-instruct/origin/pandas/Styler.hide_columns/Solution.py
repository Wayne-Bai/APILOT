import pandas as pd

# Create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)

# Hide the column headers
df_without_headers = df.set_index('Name')
print(df_without_headers)

# Hide specific keys in the columns
df_without_keys = df[['Age', 'City']].reset_index()
print(df_without_keys)
