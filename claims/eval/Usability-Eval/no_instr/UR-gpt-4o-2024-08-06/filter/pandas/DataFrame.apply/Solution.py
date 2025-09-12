import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Define a function to apply
def sum_of_squares(row):
    return sum(row**2)

# Apply the function along an axis (0 for column-wise, 1 for row-wise)
result = df.apply(sum_of_squares, axis=1)

print(result)
