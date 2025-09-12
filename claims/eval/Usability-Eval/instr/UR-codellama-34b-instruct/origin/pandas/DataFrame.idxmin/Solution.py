
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# use idxmin to return the index of the first occurrence of the minimum value in column A
print(df['A'].idxmin())
