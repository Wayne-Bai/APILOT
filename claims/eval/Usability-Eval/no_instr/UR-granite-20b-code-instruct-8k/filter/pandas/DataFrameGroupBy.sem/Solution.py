
import pandas as pd

# Assuming you have a DataFrame named df with a column 'group' and a column 'value'
# Compute standard error of the mean of groups, excluding missing values
df.groupby('group')['value'].transform(lambda x: x.fillna(x.mean()).std() / x.shape[0] ** 0.5)
