import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Function to be applied elementwise
def multiply_by_10(x):
    return x * 10

# Applying the function elementwise
df_transformed = df.applymap(multiply_by_10)

print(df_transformed)
