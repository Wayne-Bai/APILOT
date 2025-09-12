import pandas as pd

# Assuming you have two DataFrames df1 and df2

# Get rows which are different between the two DataFrames
diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
