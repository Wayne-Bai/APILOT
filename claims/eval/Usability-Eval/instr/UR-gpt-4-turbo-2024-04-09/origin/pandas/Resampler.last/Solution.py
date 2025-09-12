import pandas as pd

# Assuming 'df' is your DataFrame
df = pd.DataFrame({
    'A': [1, None, 3, 4],
    'B': ['x', 'y', None, 'z'],
    'C': [None, None, None, 10]
})

# Compute the last non-null entry of each column
last_non_null = df.ffill().iloc[-1]
print(last_non_null)
