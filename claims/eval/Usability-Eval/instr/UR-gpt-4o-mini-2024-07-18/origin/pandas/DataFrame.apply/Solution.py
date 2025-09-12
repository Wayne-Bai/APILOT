import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Define a custom function
def custom_function(x):
    return x * 2

# Apply the function along the columns (axis=0)
result_columns = df.apply(custom_function, axis=0)

# Apply the function along the rows (axis=1)
result_rows = df.apply(custom_function, axis=1)

print("Result applying function along columns:")
print(result_columns)

print("\nResult applying function along rows:")
print(result_rows)
