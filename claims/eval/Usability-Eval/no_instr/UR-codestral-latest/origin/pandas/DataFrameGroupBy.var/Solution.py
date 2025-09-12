import pandas as pd
import numpy as np

# Assuming df is your dataframe, 'group_var' is the column to group by
variances = df.dropna().groupby('group_var').var()
