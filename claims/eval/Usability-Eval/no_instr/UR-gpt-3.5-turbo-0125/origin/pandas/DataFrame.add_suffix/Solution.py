
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Suffix labels with string suffix
df.columns = [str(col) + '_suffix' for col in df.columns]

print(df)
