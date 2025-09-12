import pandas as pd

# Sample data
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Prefixing labels with a string prefix
df_prefixed = df.add_prefix('prefix_')

print(df_prefixed)
