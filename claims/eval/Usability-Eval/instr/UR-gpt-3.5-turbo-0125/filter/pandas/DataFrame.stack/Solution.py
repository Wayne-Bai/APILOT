
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Stack the prescribed level(s) from columns to index
df_stacked = df.stack()
print(df_stacked)
