import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Define a function to apply along the axis
def square(x):
    return x ** 2

# Apply the function along the columns (axis=0)
df_squared = df.apply(square, axis=0)

print(df_squared)
