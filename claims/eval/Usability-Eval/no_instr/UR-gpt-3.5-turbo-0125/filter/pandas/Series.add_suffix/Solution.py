
import pandas as pd

# Sample data
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}

# Create a DataFrame
df = pd.DataFrame(data)

# Suffix labels with string suffix
df.columns = df.columns.map(lambda x: str(x) + '_suffix')

print(df)
