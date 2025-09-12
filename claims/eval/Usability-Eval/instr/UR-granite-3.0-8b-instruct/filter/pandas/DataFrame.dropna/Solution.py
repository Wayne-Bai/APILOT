import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv('your_file.csv')  # Replace 'your_file.csv' with your actual file path

# Drop rows with missing values
df_dropped = df.dropna()

# Alternatively, you can fill missing values with a specific value or method
# df_filled = df.fillna(value=0)  # Fills missing values with 0
# df_filled = df.fillna(method='ffill')  # Fills missing values with the previous value
