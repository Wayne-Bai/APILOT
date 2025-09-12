import pandas as pd

# Define data as a dictionary
data = {
    ('A', 'one'): [1, 2, 3],
    ('A', 'two'): [4, 5, 6],
    ('B', 'one'): [7, 8, 9],
    ('B', 'two'): [10, 11, 12]
}

# Create a MultiIndex DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
