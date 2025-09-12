import pandas as pd

# Define the function
def apply_function(x):
    return x * 2

# Create a DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3, 4],
   'B': [5, 6, 7, 8]
})

# Apply the function elementwise
df = df.applymap(apply_function)

print(df)
