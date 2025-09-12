# Import pandas library
import pandas as pd

# Create a DataFrame with missing values
data = {
    'A': [1, 2, None, 4, 5],
    'B': [11, 12, 13, 14, None],
    'C': [None, 22, 23, 24, 25],
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Remove rows with missing values
df_removed_rows = df.copy()
df_removed_rows = df_removed_rows[~df_removed_rows.isnull().any(axis=1)]
print("\nDataFrame after removing rows with missing values:")
print(df_removed_rows)

# Remove columns with missing values
df_removed_cols = df.copy()
df_removed_cols = df_removed_cols.loc[:, ~df_removed_cols.isnull().any(axis=0)]
print("\nDataFrame after removing columns with missing values:")
print(df_removed_cols)

# Fill missing values with a specific value (e.g., 0)
df_filled_values = df.copy()
df_filled_values = df_filled_values.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled_values)

# Interpolate missing values
df_interpolated_values = df.copy()
df_interpolated_values = df_interpolated_values.interpolate()
print("\nDataFrame after interpolating missing values:")
print(df_interpolated_values)
