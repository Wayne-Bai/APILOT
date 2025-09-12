
import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Non-binary']}
df = pd.DataFrame(data)

# hide the index and column headers
df.index.rename('', inplace=True)
df.columns.rename('', inplace=True)

print(df)
