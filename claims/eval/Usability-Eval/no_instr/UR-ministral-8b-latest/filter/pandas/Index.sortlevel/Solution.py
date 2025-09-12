import pandas as pd

# Sample MultiIndex DataFrame
df = pd.DataFrame({
    ('A', 'B'): [10, 20, 30],
    ('A', 'C'): [15, 25, 35],
    ('D', 'B'): [40, 50, 60],
    ('D', 'C'): [45, 55, 65]
})

# Setting the MultiIndex
df.columns = pd.MultiIndex.from_tuples(df.columns)

# Sorting the Index
sorted_df = df.T / 2  # Sorting by index levels
sorted_df.columns = [tuple(sorted(col)) for col in sorted_df.columns]

# Display sorted DataFrame
print(sorted_df)
