import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Define a function to apply
def square(x):
    return x ** 2

# Apply the function elementwise using the DataFrame's apply method
df_squared = df.applymap(square)

print(df_squared)
