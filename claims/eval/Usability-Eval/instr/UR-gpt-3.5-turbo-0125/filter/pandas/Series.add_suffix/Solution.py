
import pandas as pd

# Sample data
data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': ['A', 'B', 'C', 'D', 'E']}

# Create a DataFrame
df = pd.DataFrame(data)

# Suffix labels with string suffix
df.columns = df.columns + '_suffix'

print(df)
