import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Value': [1, 2, 3, 4, 5, None]
}

df = pd.DataFrame(data)

# Function to compute standard error of the mean
def standard_error_of_mean(group):
    return group.std(ddof=0) / group.count()**0.5

# Group by 'Group' and compute the standard error of the mean
result = df.groupby('Group')['Value'].apply(standard_error_of_mean).reset_index(name='Standard Error of Mean')

print(result)
