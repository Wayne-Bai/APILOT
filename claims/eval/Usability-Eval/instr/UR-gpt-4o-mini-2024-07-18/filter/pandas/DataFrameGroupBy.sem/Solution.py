import pandas as pd

# Sample DataFrame
data = {
    'group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'values': [10, 15, None, 10, 20, 30, None, 40]
}

df = pd.DataFrame(data)

# Compute standard error of the mean for each group, excluding missing values
grouped = df.groupby('group')['values']
mean = grouped.mean()
count = grouped.count()
std_dev = grouped.std(ddof=0)  # Use population standard deviation
standard_error = std_dev / (count ** 0.5)

# Convert to DataFrame for better readability
result = pd.DataFrame({'mean': mean, 'standard_error': standard_error}).reset_index()
print(result)
