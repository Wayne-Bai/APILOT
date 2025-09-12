import pandas as pd

# Create a DataFrame example
data = {
    'A': [1, 2, 3, None, 5],
    'B': [0, None, 2, 3, 4],
    'C': [None, 1, None, 3, 5]
}
df = pd.DataFrame(data)

# Compute standard deviation of each group, excluding missing values
std_dev = df.groupby(df.columns, axis=1).std()

print(std_dev)
