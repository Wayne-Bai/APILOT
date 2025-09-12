import pandas as pd

# Function to be applied
def square(x):
    return x*x

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Apply the function elementwise
df = df.apply(square)

print(df)
