
import pandas as pd

# Assuming df is the DataFrame that needs to have its index reset
df.reset_index(drop=True, inplace=True)

# If df has a multi-index and only specific level needs to be reset, use the following code
# df.reset_index(level=0, inplace=True)  # Replace 0 with the specific level you want to reset
