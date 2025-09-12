import pandas as pd

# Create a DataFrame with a MultiIndex
df = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'E': ['E0', 'E1', 'E2', 'E3']
}, index=pd.MultiIndex.from_tuples([(i, j) for i in range(4) for j in range(3)]))

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Reset the index of the DataFrame
df = df.reset_index(drop=True)

# Print the DataFrame after resetting the index
print("\nDataFrame after resetting the index:")
print(df)
