
import pandas as pd

# Example data
data = {
    'codes': [1, 2, 3, 1, 2, 3, 1],
    'categories': ['A', 'B', 'C', 'A', 'B', 'C', 'A']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert to categorical type using the 'codes' column
df['codes'] = pd.Categorical(df['codes'])

# Convert to categorical type using the 'categories' column
df['categories'] = pd.Categorical(df['categories'])

# Display the DataFrame with categorical types
print(df)
print(df.dtypes)
