import pandas as pd
import numpy as np

# Assume df is your DataFrame and 'column_name' is the column you want to calculate the rolling mean on
df['rolling_mean'] = df['column_name'].rolling(window=3).mean()
