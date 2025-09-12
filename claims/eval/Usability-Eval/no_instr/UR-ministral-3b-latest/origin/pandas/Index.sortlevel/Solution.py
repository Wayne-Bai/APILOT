import pandas as pd

# Example DataFrame with MultiIndex
df = pd.DataFrame({
    ('A', 'Page1'): [1, 2, 3],
    ('A', 'Page2'): [4, 5, 6],
    ('B', 'Page1'): [7, 8, 9]
}, index=[0, 2, 1])

# Sorting the Index for internal compatibility with MultiIndex
df.sort_index(inplace=True)

print(df)
