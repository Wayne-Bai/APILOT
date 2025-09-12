import pandas as pd

# Assuming df is the DataFrame
# Reset the index of the DataFrame, and use the default one instead
df_reset = df.reset_index(drop=True)

# If the DataFrame has a MultiIndex, removing one level
# df_reset = df.reset_index(level=0, drop=True)

# If you want to remove all levels of MultiIndex
# df_reset = df.reset_index(drop=True)
