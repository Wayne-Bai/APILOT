import pandas as pd

# Example data
data = {
    'text': [
        "apple,banana,cherry",
        "grape,melon,dumpy"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Use str.split() to split strings around the given separator
df['split_strings'] = df['text'].str.split(',')

print(df)
