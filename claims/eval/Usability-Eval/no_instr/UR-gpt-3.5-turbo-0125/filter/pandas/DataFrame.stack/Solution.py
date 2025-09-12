
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}

df = pd.DataFrame(data, index=['X', 'Y', 'Z', 'W'])

# Stack the prescribed level(s) from columns to index
df_stacked = df.stack()

print(df_stacked)
