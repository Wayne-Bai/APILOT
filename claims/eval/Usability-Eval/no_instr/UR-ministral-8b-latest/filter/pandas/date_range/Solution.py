import pandas as pd
import numpy as np

# Generate a date range
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='MS')

# Create a DataFrame with the generated date range
df = pd.DataFrame(date_range, columns=['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

print(df)
