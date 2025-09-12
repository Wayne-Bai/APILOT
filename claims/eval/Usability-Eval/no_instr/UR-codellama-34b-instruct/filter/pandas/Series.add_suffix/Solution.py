
import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)

# add a new column with the suffix 'label' to each row
df['Label'] = df['Name'].str.cat(sep='_')
print(df)
