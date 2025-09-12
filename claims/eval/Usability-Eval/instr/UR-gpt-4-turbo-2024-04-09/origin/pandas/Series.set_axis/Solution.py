import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Assigning a new index to the DataFrame
new_index = ['one', 'two', 'three']
df.index = new_index

print(df)
