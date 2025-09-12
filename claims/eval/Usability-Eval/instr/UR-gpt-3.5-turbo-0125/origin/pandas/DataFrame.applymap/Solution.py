
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Define a function to apply on each element
def square(x):
    return x ** 2

# Apply the function element-wise to the dataframe
df = df.applymap(square)

print(df)
