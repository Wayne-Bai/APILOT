import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['aaware', 'bared', 'cubic', 'dynamo', 'emerge']
})

# Define a mapping or function
mapping = {
    'aaware': 'aware',
    'bared': 'bare',
    'cubic': 'cube',
    'emerge': 'emergence'
}

def custom_mapping(value):
    value = value.lower().replace('_', '').strip()
    return value

# Apply the mapping
df['B'] = df['B'].replace(mapping)
df['A'] = df['A'].apply(custom_mapping)

print(df)
