import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Function to apply elementwise
def add_five(x):
    return x + 5

# Applying the function elementwise
result_df = df.applymap(add_five)

print(result_df)
