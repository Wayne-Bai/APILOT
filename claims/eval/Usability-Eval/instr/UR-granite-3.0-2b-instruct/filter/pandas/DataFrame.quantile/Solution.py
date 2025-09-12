import pandas as pd

# Assuming df is your DataFrame and quantile is the desired quantile (e.g., 0.5 for median)
def get_quantile_values(df, quantile):
    return df.quantile(quantile).reset_index()

# Example usage:
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

quantile_values = get_quantile_values(df, 0.5)
print(quantile_values)
