import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Define a custom function
def custom_function(row):
    # Example: Sum of the row values
    return row.sum()

# Apply the custom function along the rows (axis=1)
result = df.apply(custom_function, axis=1)

print(result)
