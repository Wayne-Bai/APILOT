import pandas as pd

def standard_error_of_mean(df, group_col, value_col):
    # Compute the mean and standard deviation for each group
    group_stats = df.groupby(group_col)[value_col].agg(['mean', 'std', 'count'])
    
    # Calculate standard error of the mean
    group_stats['sem'] = group_stats['std'] / (group_stats['count'] ** 0.5)
    
    return group_stats['sem']

# Example usage:
# df = pd.DataFrame({
#     'group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
#     'value': [10, 20, 10, None, 30, 40, 50]
# })
# print(standard_error_of_mean(df, 'group', 'value'))
