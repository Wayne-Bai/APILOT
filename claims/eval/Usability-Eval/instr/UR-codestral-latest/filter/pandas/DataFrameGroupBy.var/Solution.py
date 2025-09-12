import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'group' is the column containing the groups
df.dropna(subset=['column_name']).groupby('group')['column_name'].var()
