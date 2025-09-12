import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Assign desired index to rows (axis=0)
df.index = ['x', 'y', 'z']

# Display the modified DataFrame
print(df)
