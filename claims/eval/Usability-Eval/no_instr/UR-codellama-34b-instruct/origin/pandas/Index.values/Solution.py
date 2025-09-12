import pandas as pd

# Define the DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Male']}
df = pd.DataFrame(data)

# Define the index
index_col = 'Name'

# Return an array representing the data in the index
result = df[index_col].to_numpy()
print(result)
