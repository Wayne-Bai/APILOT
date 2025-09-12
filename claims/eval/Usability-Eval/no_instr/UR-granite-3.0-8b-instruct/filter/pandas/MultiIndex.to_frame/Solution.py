import pandas as pd

# Create a DataFrame with a MultiIndex
data = {
    ('a', 'x'): 1,
    ('a', 'y'): 2,
    ('b', 'x'): 3,
    ('b', 'y'): 4
}
index = pd.MultiIndex.from_tuples(list(data.keys()), names=['level1', 'level2'])
df = pd.DataFrame(data, index=index)

# Create a DataFrame with the levels of the MultiIndex as columns
df_columns = df.columns.to_frame().reset_index(drop=True)
df_columns.columns = ['level1', 'level2']
