import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Define a function that will be applied to each element
def add_one(x):
    return x + 1

# Apply the function elementwise using the DataFrame's applymap method
df = df.applymap(add_one)

print(df)
