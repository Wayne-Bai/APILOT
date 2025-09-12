import pandas as pd

# Assuming df is your DataFrame
first_non_null = df.apply(lambda x: x.dropna().iloc[0] if not x.dropna().empty else None)
