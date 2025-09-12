
import pandas as pd

# create sample data
df = pd.DataFrame({'A': [1, 2, 3, 4, np.nan], 'B': [5, 6, 7, 8, np.nan]})

# print the index of first occurrence of minimum over requested axis
print(df.idxmin())
