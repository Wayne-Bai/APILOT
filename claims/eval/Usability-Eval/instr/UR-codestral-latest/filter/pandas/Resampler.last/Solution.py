import pandas as pd

# Assuming df is your DataFrame
last_non_null_entries = df.dropna(how='all').iloc[-1]
