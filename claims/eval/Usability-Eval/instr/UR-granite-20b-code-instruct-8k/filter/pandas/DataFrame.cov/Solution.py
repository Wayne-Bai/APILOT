import pandas as pd

# Assuming df is your DataFrame
# Replace 'col1' and 'col2' with the names of the columns you want to compute the covariance for
cov = df[['col1', 'col2']].cov().loc['col1', 'col2']
