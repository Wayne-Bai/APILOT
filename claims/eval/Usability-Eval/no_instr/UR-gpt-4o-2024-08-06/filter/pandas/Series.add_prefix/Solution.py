import pandas as pd

# Sample DataFrame
data = {'Label': ['Label1', 'Label2', 'Label3']}
df = pd.DataFrame(data)

# Prefix for labels
prefix = 'Prefix_'

# Applying prefix to all labels in the 'Label' column
df['Label'] = df['Label'].apply(lambda x: prefix + x)

print(df)
