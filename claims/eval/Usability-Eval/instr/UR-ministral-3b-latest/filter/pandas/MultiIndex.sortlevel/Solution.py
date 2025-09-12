import pandas as pd

# Sample MultiIndex DataFrame
data_multiindex = {
    ('A', 'apple'): [10, 20, 30],
    ('B', 'banana'): [40, 50, 60],
    ('A', 'orange'): [70, 80, 90],
    ('B', 'grape'): [100, 110, 120]
}

index_multi = pd.MultiIndex.from_tuples(data_multiindex.keys(), names=['letter', 'fruit'])
df = pd.DataFrame(data_multiindex, index=index_multi)

# Sort the DataFrame by the "letter" level
df.sort_index(level=0)
