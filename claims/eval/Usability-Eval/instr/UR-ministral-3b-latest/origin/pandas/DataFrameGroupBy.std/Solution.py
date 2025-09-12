import pandas as pd

# Assuming df is your dataframe
groups = df.groupby('group_column')
df_std = pd.concat({k: groups[k].std() for k in groups.groups})
