import pandas as pd

# Assuming you have a DataFrame called 'df' and you want to add a string prefix 'X_' to all column names
df.columns = ['X_' + col for col in df.columns]
