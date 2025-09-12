
import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)

# assign the desired index to the given axis (in this case, the "name" column)
df = df.set_index('name')
