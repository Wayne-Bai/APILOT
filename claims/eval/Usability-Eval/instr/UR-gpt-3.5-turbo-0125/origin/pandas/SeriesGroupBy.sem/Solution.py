
import pandas as pd

def standard_error_of_mean(df, group_by_col, value_col):
    grouped = df.groupby(group_by_col)[value_col]
    mean = grouped.mean()
    group_counts = grouped.count()
    std_err = grouped.std() / (group_counts ** 0.5)
    return std_err

# Example Usage
data = {'Group': [1, 1, 2, 2, 3, 3],
        'Value': [10, 20, 30, None, 50, 60]}
df = pd.DataFrame(data)

std_err = standard_error_of_mean(df, 'Group', 'Value')
print(std_err)
