import pandas as pd

# Creating a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Defining a function to apply to each column
def multiply_by_two(x):
    return x * 2

# Applying function along the axis 0 (down the rows)
result = df.apply(multiply_by_two)

print(result)
