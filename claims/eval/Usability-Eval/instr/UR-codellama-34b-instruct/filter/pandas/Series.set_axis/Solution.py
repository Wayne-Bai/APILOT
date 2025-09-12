
import pandas as pd

# Sample data
data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [27, 31, 23],
        'City': ['New York', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Assign desired index to axis 0 (rows)
df.index = df['Name'].str.lower() + '_' + df['Age'].astype(str)

# Print the result
print(df)
