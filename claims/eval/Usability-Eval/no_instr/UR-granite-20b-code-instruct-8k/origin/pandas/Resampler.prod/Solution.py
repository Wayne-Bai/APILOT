import pandas as pd

# Assuming you have a DataFrame named 'df' with a column named 'group' and a column named 'value'
# Compute prod of group values
result = df.groupby('group')['value'].prod()

print(result)
