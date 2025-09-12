import pandas as pd

def custom_quantile(df, q, axis=0):
    if axis == 0:
        sorted_df = df.sort_values(by=df.columns[0], axis=0)
    else:
        sorted_df = df.sort_values(by=df.index[0], axis=1)
    
    n = len(sorted_df) if axis == 0 else len(sorted_df.columns)
    index = (n - 1) * q
    floor_index = int(index)
    ceil_index = floor_index + 1 if floor_index < index else floor_index
    
    if floor_index == ceil_index:
        return sorted_df.iloc[floor_index] if axis == 0 else sorted_df.iloc[:, floor_index]
    else:
        lower_value = sorted_df.iloc[floor_index] if axis == 0 else sorted_df.iloc[:, floor_index]
        upper_value = sorted_df.iloc[ceil_index] if axis == 0 else sorted_df.iloc[:, ceil_index]
        return lower_value + (upper_value - lower_value) * (index - floor_index)

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [10, 20, 30, 40, 50]
# })
# quantile_value = custom_quantile(df, 0.5, axis=0)
# print(quantile_value)
