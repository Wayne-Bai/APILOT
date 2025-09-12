import pandas as pd

def quantile_values(df, axis, quantile):
    if axis == 0:  # Rows
        return df.quantile(quantile)
    elif axis == 1:  # Columns
        return df.quantile(quantile, axis=1)
    else:
        raise ValueError("Axis must be either 0 or 1")

# Example usage:
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)

print(quantile_values(df, 0, 0.5))  # Print the median value of each column
print(quantile_values(df, 1, 0.5))  # Print the median value of each row
