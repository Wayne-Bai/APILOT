
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Define a function to double the values
def double(x):
    return x * 2

# Apply the function elementwise to the dataframe
df = df.applymap(double)

print(df)
