import pandas as pd

# Sample data with MultiIndex
data = {
    ('A', 'X'): [1, 2, 3],
    ('A', 'Y'): [4, 5, 6],
    ('B', 'X'): [7, 8, 9],
    ('B', 'Y'): [10, 11, 12]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
