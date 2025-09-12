import pandas as pd

# Sample DataFrame
data = {'labels': ['label1', 'label2', 'label3']}
df = pd.DataFrame(data)

# Prefix to be added
prefix = 'prefix_'

# Prefixing the labels
df['prefixed_labels'] = prefix + df['labels']

# Display the DataFrame
print(df)
