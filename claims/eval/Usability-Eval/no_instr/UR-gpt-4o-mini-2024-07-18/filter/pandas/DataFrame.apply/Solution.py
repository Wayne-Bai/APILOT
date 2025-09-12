import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Define a function to apply
def my_function(x):
    return x.sum()

# Apply the function along the columns (axis=0)
result_columns = df.apply(my_function, axis=0)

# Apply the function along the rows (axis=1)
result_rows = df.apply(my_function, axis=1)

print("Result applied along columns:")
print(result_columns)

print("\nResult applied along rows:")
print(result_rows)
