import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)

# perform a reduction operation on the dataframe
result = df.sum()

# print the result
print(result)
