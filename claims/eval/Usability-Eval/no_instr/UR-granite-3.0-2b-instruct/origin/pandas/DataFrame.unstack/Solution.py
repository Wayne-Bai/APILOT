import pandas as pd

# Sample data
data = {
    'A': {'X': 1, 'Y': 2, 'Z': 3},
    'B': {'X': 4, 'Y': 5, 'Z': 6},
    'C': {'X': 7, 'Y': 8, 'Z': 9}
}

# Create a MultiIndex DataFrame
df = pd.DataFrame(data).set_index(['A', 'B'])

# Pivot the level of the index labels
df_pivoted = df.pivot(level=0)

print(df_pivoted)
