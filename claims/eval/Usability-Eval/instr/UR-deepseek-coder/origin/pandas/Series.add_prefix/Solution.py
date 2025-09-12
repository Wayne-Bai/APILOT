import pandas as pd

# Sample DataFrame
data = {
    'labels': ['apple', 'banana', 'cherry']
}
df = pd.DataFrame(data)

# Prefix labels with a string prefix
prefix = 'fruit_'
df['labels'] = prefix + df['labels']

print(df)
