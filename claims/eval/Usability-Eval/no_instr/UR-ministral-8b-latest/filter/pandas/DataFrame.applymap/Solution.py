import pandas as pd

# Example dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Function to apply to each element
def example_function(x):
    return x + 1

# Apply the function to each element elementwise
df = df.applymap(example_function)

print(df)
