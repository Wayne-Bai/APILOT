import pandas as pd

# Assuming df is your DataFrame and 'prefix' is the string you want to prefix
df.columns = ['prefix_' + col for col in df.columns]
