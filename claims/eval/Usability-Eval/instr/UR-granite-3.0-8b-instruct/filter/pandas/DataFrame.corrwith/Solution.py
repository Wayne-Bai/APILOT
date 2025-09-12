import pandas as pd

# Assuming df is your DataFrame
# Compute pairwise correlation
correlation = df.corr()

# If you want to compute pairwise correlation for specific columns
# correlation = df[['column1', 'column2']].corr()
