import pandas as pd

def compare_dataframes(df1, df2):
    # Check if both DataFrames have the same columns
    common_columns = df1.columns.intersection(df2.columns)
    if common_columns.empty:
        return f"DataFrames do not have any common columns"

    # Create empty lists to store differences
    differences = []
    common_indices = df1.index.intersection(df2.index)

    # Compare data for each common column across common indices
    for column in common_columns:
        column_diff = pd.DataFrame(columns=['Index', 'Column name', 'Difference'], index=set(df1.index) | set(df2.index))
        for idx in common_indices:
            if df1.loc[idx, column] != df2.loc[idx, column]:
                column_diff.at[idx, 'Index'] = idx
                column_diff.at[idx, 'Column name'] = column
                column_diff.at[idx, 'Difference'] = df1.loc[idx, column] - df2.loc[idx, column]

        differences.append(column_diff[column_diff['Difference'].notna()])

    return differences

# Example usage
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df2 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [5, 6, 7],
    'C': [7, 10, 9]
})

differences = compare_dataframes(df1, df2)
for diff in differences:
    print(diff)
