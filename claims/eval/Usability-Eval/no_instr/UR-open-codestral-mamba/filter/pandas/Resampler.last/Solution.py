import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan]
})

# You can get the last non-null entries using the following line of code
last_non_null = df.apply(lambda x: x.dropna().last_valid_index())
