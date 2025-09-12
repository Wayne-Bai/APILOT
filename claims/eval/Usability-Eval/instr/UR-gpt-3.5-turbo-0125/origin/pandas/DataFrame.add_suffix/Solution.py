
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4],
        'B': ['apple', 'banana', 'cherry', 'date']}
df = pd.DataFrame(data)

# Suffix labels with string suffix
df.columns = df.columns + '_suffix'

print(df)
