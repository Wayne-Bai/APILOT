import pandas as pd

# create a dict with the MultiIndex levels and their respective values
data = {'level_1': ['a', 'b'], 'level_2': [1, 2], 'level_3': [3.0, 4.0]}

# create a DataFrame from the dict using the `DataFrame` constructor with the specified column ordering
df = pd.DataFrame(data, columns=['level_1', 'level_2', 'level_3'])
