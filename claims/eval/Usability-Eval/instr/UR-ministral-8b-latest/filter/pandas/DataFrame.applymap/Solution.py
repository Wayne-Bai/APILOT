import pandas as pd

# Sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Function to apply
def custom_function(x):
    return x ** 2

# Applying the function elementwise to each element of the DataFrame
df_applied = df.applymap(custom_function)

print(df_applied)
