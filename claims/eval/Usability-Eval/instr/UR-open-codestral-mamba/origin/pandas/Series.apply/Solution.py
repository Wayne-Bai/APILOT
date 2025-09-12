import pandas as pd

# Create a pandas Series
s = pd.Series([1, 2, 3, 4, 5])

# Function to apply on Series
def func(x):
    return x * 2

# Invoke function on values of Series
s_new = s.apply(func)

print(s_new)
