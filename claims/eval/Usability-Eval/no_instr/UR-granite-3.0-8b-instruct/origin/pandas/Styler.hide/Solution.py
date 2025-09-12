import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame(...)

# Hide the entire index
df.index.name = None

# Hide the entire column headers
df.columns.name = None

# Hide specific rows
df = df.drop([0, 2], axis=0)

# Hide specific columns
df = df.drop(['Column1', 'Column3'], axis=1)
