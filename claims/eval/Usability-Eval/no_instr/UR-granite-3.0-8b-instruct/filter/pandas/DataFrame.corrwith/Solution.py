import pandas as pd

# Assuming df is your DataFrame
corr_matrix = df.corr()

# If you want to see the correlation matrix as a table
corr_table = corr_matrix.style.set_properties(**{'text-align': 'center'})

print(corr_table)
