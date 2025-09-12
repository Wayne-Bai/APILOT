
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'group': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'value': [10, 20, 30, 40, 50, 60]})

# Group the DataFrame by 'group' column and compute min value for each group
df_grp = df.groupby('group')['value'].min()

# Print the minimum value for each group
print(df_grp)
