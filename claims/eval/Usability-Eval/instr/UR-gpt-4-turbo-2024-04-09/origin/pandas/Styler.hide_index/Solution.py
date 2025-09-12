import pandas as pd

# Creating a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Suppress the display of indices in the DataFrame
with pd.option_context('display.index', False):
    print(df)
