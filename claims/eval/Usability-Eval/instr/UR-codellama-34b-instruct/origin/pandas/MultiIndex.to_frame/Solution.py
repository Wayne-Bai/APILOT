import pandas as pd

# Create a dictionary with the levels of the MultiIndex as keys and their corresponding values as values
levels = {'a': ['x', 'y'], 'b': ['z']}

# Use the DataFrame constructor to create a new DataFrame with the levels of the MultiIndex as columns
df = pd.DataFrame(levels, index=['c'])
