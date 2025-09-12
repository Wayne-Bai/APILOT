import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv('your_file.csv')

# Drop rows with missing values
df_dropped = df.dropna()

# Or fill missing values with a specific value
df_filled = df.fillna(value='filled_value')
