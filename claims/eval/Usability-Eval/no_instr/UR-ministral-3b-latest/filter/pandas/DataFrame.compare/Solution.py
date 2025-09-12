import pandas as pd

def compare_dfs(df1, df2):
    differences = df1.compare(df2)

    if differences.isnull().any().any():
        print("DataFrames have differences in non-required columns or missing values.")

    display(differences)
    return differences

# Example usage
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

compare_dfs(df1, df2)
