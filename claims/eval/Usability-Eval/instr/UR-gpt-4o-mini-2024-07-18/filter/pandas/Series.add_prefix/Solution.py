import pandas as pd

# Sample DataFrame
data = {
    'labels': ['apple', 'banana', 'cherry']
}
df = pd.DataFrame(data)

# Define the prefix
prefix = 'fruit_'

# Prefix the labels
df['prefixed_labels'] = prefix + df['labels']

print(df)
