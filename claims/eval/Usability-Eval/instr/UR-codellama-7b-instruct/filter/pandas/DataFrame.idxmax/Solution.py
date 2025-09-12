
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# find index of first occurrence of maximum over requested axis
print(df.idxmax())
