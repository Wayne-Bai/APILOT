import pandas as pd

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Assigning a new index to the DataFrame
new_index = ['one', 'two', 'three']
df.index = new_index

print(df)
