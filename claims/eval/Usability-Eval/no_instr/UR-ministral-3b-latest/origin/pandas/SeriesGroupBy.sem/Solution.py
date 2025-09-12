import pandas as pd

# Sample data
data = {
    'Group1': [20, 21, 30, 25, 19, None, 23],
    'Group2': [30, None, 21, 29, 24, 26, 35],
}

df = pd.DataFrame(data)

# Define a function to compute the standard error of the mean excluding NaNs
def standard_error_of_mean(group):
    n = len(group)
    sample_mean = group.mean()
    variance = group.var(ddof=1)
    sem = variance / (n - 1) ** 0.5
    return sem

# Apply the function to each group
df['Standard Error of Mean'] = df.apply(lambda row: standard_error_of_mean(row) if not pd.isna(row['Standard Error of Mean']) else row, axis=1)

print(df)
