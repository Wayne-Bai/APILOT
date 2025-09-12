import pandas as pd

# Assuming you have a DataFrame called 'df' and you want to perform a reduction operation.
# For example, let's calculate the mean of all numeric columns in the DataFrame.
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': [100, 200, 300]
})

# Performing the reduction operation to get the mean of all numeric columns.
result = df.mean().mean()

print(result)
