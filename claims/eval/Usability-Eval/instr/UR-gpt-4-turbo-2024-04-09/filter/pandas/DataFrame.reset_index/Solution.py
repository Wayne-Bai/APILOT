import pandas as pd

# Sample DataFrame with a MultiIndex
data = {
    'score': [25, 32, 45, 58]
}
index = pd.MultiIndex.from_arrays([
    ['A', 'A', 'B', 'B'],
    ['a', 'b', 'a', 'b']
], names=['upper', 'lower'])

df = pd.DataFrame(data, index=index)

# Reset the index of the DataFrame, using the default one
df_reset = df.reset_index()

print(df_reset)
