import pandas as pd

# Assuming df is your DataFrame and 'level1' and 'level2' are the hierarchical index labels
df = pd.DataFrame({
    ('level1', 'level2'): [
        ('A', 'X'),
        ('A', 'Y'),
        ('B', 'X'),
        ('B', 'Y')
    ]
})

# Set 'level1' and 'level2' as the index
df.set_index(['level1', 'level2'], inplace=True)

# Pivot the index labels
df.reset_index(level=['level1', 'level2'], inplace=True)
df.rename(columns={'index': 'pivoted_index'}, inplace=True)

print(df)
