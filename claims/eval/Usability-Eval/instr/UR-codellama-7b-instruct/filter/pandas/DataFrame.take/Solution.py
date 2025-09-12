
import pandas as pd

# Create a sample dataframe
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

# Return the elements in the first column along axis=0 (rows)
print(df.loc[0])  # Output: 1

# Return the elements in the second column along axis=1 (columns)
print(df.iloc[:, 1])  # Output: 5
