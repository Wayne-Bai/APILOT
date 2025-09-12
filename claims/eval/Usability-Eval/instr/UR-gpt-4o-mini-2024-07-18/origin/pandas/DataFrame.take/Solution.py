import pandas as pd

# Sample DataFrame
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [60, 70, 80, 90, 100],
    'C': [110, 120, 130, 140, 150]
}

df = pd.DataFrame(data)

# Define positional indices
indices = [0, 2, 4]

# Return elements in the given positional indices along axis 0 (rows)
result_rows = df.iloc[indices]

# Return elements in the given positional indices along axis 1 (columns)
result_columns = df.iloc[:, indices]

print("Selected Rows:\n", result_rows)
print("\nSelected Columns:\n", result_columns)
