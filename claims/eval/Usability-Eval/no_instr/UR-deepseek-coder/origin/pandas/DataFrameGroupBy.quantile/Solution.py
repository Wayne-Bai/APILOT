import pandas as pd

def group_quantile(df, group_col, value_col, q):
    return df.groupby(group_col)[value_col].quantile(q)

# Example usage:
# data = {'Group': ['A', 'A', 'B', 'B', 'B'], 'Value': [10, 20, 30, 40, 50]}
# df = pd.DataFrame(data)
# result = group_quantile(df, 'Group', 'Value', 0.5)
# print(result)
