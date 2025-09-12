# Import the pandas library
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
})

# Function to add suffix to column labels
def add_suffix_columns(df, suffix):
    df.columns = [col + suffix for col in df.columns]
    return df

# Add a suffix to column labels
df = add_suffix_columns(df, '_suffix')

print(df)
