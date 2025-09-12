import pandas as pd

# Creating a sample DataFrame
data = {
    'A': [1, 0, None, True, False],
    'B': ['apple', 0, None, True, False]
}
df = pd.DataFrame(data)

# Function to check for any truthy value
def hasTruthy(df):
    return df.any(axis=1).any()

# Checking if any element is truthy
print(hasTruthy(df))
