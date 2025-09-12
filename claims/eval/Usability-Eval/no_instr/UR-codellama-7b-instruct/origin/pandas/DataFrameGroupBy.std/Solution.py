
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, np.nan], 'B': [5, 6, 7, 8, 9], 'C': [10, 11, 12, 13, 14]})

# compute standard deviation for each group, excluding missing values
df.groupby('A').std()
