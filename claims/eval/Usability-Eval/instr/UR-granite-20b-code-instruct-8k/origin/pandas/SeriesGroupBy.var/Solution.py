import pandas as pd

# Assuming df is the DataFrame and 'column' is the column to compute variance for
# 'group' is the column to group by

result = df.groupby('group')[column].var(skipna=True)
