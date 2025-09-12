import pandas as pd

# Assuming df is your DataFrame and 'column' is the column you want to compute the standard deviation for
df = pd.DataFrame({
    'column': [1, 2, None, 4, 5]
})

# Filter out missing values
df_no_missing = df.dropna(subset=['column'])

# Compute standard deviation of groups
std_dev = df_no_missing['column'].std()

print(std_dev)
