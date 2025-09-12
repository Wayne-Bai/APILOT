
import pandas as pd

# Create a sample dataframe
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

# Prefix the column labels with "Prefix_".
# This creates a new dataframe with the prefixed column labels.
prefixed_df = df.add_prefix('Prefix_')

# Print the new dataframe
print(prefixed_df)
