import pandas as pd

# Assuming df is your DataFrame and 'axis' is either 'rows' or 'columns'
# and 'indices' is a list of positional indices

if axis == 'rows':
    return df.iloc[indices]
else:
    return df.loc[:, indices]
