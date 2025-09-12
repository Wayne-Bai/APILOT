import pandas as pd

# Sample DataFrame with a MultiIndex
arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=('letters', 'numbers'))
df = pd.DataFrame({'value': [10, 20, 30, 40]}, index=index)

# Reset the index to remove the MultiIndex and use the default index
df_reset = df.reset_index()

# Display the reset DataFrame
print(df_reset)
