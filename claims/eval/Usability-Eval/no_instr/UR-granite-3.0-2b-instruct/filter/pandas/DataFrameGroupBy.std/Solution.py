import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to compute the standard deviation for
df = pd.DataFrame({
    'column_name': [1, 2, 3, 4, 5, None, 7, 8, 9, 10]
})

# Compute standard deviation of groups, excluding missing values
std_dev = df['column_name'].groupby(df['column_name'].apply(lambda x: x if pd.notna(x) else None)).std().mean()

print(std_dev)
