import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, None, 6, 7, None]
}

df = pd.DataFrame(data)

# Function to compute standard error of the mean
def std_error_of_mean(series):
    return series.std() / (series.count() ** 0.5)

# Group by 'Group' and compute standard error of the mean for each group
result = df.groupby('Group')['Value'].agg(std_error_of_mean)

print(result)
