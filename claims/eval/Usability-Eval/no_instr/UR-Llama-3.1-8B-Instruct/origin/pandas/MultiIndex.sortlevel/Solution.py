import pandas as pd

# Creating a MultiIndex DataFrame
data = {
    ('North', 'City1'): {'Year1': 100, 'Year2': 200},
    ('North', 'City2'): {'Year1': 300, 'Year2': 400},
    ('South', 'City1'): {'Year1': 500, 'Year2': 600},
    ('South', 'City2'): {'Year1': 700, 'Year2': 800}
}
index = pd.MultiIndex.from_tuples(data.keys())
df = pd.DataFrame(data, index=index)

print("Original DataFrame:")
print(df)

# Sorting the MultiIndex at the 'Region' level
df = df.sort_index(level='Region')

print("\nDataFrame after sorting at 'Region' level:")
print(df)
