
import pandas as pd

# Create a sample Series
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Create a custom function to apply
def custom_function(x):
    return x ** 2

# Apply the custom function to a specific column in the DataFrame
df['A'] = df['A'].apply(custom_function)

print(df)
