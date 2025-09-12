
import pandas as pd

# Sample data
data = {'A': [1, 2, None, 4],
        'B': [None, 5, 6, 7],
        'C': [9, None, None, 12]}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_non_null = {col: df[col][df[col].notnull()].iloc[-1] for col in df.columns}

print(last_non_null)
