
import pandas as pd

# create sample data
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print(df)

# stack the prescribed levels from columns to index
stacked_df = df.stack(level=0)
print(stacked_df)
