import pandas as pd
# Assuming you have a DataFrame called df and a column called 'group'
product = df.groupby('group')['column'].prod()
