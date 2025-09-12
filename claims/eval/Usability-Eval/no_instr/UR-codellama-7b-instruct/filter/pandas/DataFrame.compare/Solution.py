
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# compare to another dataframe
other_df = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})

# show differences
print(pd.concat([df.isin(other_df), other_df], axis=1))
