import pandas as pd

def compute_standard_error_of_mean(df, group_column, value_column):
    # Group by the specified column
    grouped = df.groupby(group_column)[value_column]
    
    # Compute the standard error of the mean for each group
    standard_error = grouped.apply(lambda x: x.std() / (x.count() ** 0.5))
    
    return standard_error

# Example usage
data = {
    'group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'value': [10, 20, None, 30, 10, None, 20]
}

df = pd.DataFrame(data)
result = compute_standard_error_of_mean(df, 'group', 'value')
print(result)
