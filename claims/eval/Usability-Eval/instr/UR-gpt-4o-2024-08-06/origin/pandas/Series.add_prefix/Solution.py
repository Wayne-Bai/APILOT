import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Define your prefix
prefix = 'Prefix_'

# Add prefix to the column labels
df.columns = [prefix + col for col in df.columns]

print(df)
