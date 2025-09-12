import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set MultiIndex for demonstration purposes
df.columns = pd.MultiIndex.from_tuples([('X', 'A'), ('X', 'B'), ('Y', 'C')])

# Stack the prescribed level(s) from columns to index
stacked_df = df.stack(level=0)

# Display the result
print(stacked_df)
