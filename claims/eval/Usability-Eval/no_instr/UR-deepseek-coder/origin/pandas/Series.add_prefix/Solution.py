import pandas as pd

# Sample DataFrame
data = {
    'labels': ['A', 'B', 'C', 'D']
}
df = pd.DataFrame(data)

# Prefix labels with string 'prefix_'
df['labels'] = 'prefix_' + df['labels']

print(df)
