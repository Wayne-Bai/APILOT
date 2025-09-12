import pandas as pd

# Assuming 'data' is your data
df = pd.DataFrame(data)

# If you have a MultiIndex, you can convert it to columns using the unstack() method
df = df.unstack()

# The levels of the MultiIndex are now the columns of the DataFrame
print(df.columns)