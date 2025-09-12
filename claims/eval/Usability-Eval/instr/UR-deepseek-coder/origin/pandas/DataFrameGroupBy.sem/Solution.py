import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, None, 6, 7, 8]
}

df = pd.DataFrame(data)

# Function to compute standard error of the mean
def standard_error_of_mean(series):
    return series.std() / (len(series) ** 0.5)

# Group by 'Group' and compute the standard error of the mean for each group
result = df.groupby('Group')['Value'].agg(lambda x: standard_error_of_mean(x.dropna()))

print(result)
