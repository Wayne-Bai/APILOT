import pandas as pd

# Assuming you have a DataFrame called 'df' and a column called 'group'
variance = df.groupby('group')['column'].var()

print(variance)
