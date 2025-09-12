import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3, 4, 5],
   'B': [5, 4, 3, 2, 1]
})

# Define a function to apply elementwise
def elementwise_func(x):
    return x * 2

# Apply the function to the DataFrame elementwise
df_result = df.applymap(elementwise_func)

print(df_result)
