import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Values': [10, 15, None, 20, 30, None, 25]
}

df = pd.DataFrame(data)

# Define a function to compute the standard error of the mean
def standard_error(x):
    return x.std(ddof=1) / (len(x.dropna()) ** 0.5)

# Group by 'Group' and compute the standard error of the mean for 'Values' column
result = df.groupby('Group')['Values'].apply(standard_error)

print(result)
