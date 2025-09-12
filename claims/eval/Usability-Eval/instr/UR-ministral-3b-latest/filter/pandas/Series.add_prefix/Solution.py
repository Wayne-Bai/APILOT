import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]}
df = pd.DataFrame(data)

# Sample List of Prefixes
prefixes = ['Mr.', 'Ms.', 'Sir.']

# Function to add prefixes to names
def add_prefixes(df, prefixes):
    for idx, value in df['Name'].items():
        prefix = prefixes[idx % len(prefixes)]
        df['Name'][idx] = f"{prefix} {value}"
    return df

# Apply the function
df = add_prefixes(df, prefixes)

print(df)
