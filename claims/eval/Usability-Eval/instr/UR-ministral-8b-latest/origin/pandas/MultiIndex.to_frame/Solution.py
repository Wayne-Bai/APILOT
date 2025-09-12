import pandas as pd

# Example MultiIndex
index = pd.MultiIndex.from_tuples(
    [('a', 'x'), ('a', 'y'), ('b', 'x'), ('b', 'y')],
    names=['level1', 'level2']
)

# Create a DataFrame with the MultiIndex as columns
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
}
df = pd.DataFrame(data, index=index)

# Set column names
df.columns.name = 'index'
df = df.unstack()

# Set column names directly
df.columns = ['A', 'B']

# Print the resulting DataFrame
print(df)
