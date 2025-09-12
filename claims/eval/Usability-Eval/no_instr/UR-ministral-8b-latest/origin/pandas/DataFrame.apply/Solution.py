import pandas as pd

# Example functionality to demonstrate applying a function along an axis of the DataFrame
def apply_function(data):
    return data * 2  # Example function: multiply each element by 2

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Apply the function along axis 0 (rows)
result_by_row = df.apply(apply_function, axis=0)

# Apply the function along axis 1 (columns)
result_by_col = df.apply(apply_function, axis=1)

print("Result by row:")
print(result_by_row)
print("\nResult by column:")
print(result_by_col)
