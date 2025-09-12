import pandas as pd
import numpy as np

# Set the starting date and frequency for the datetime index
start_date = '2023-01-01'
frequency = 'H'  # Hourly frequency

# Generate the DatetimeIndex
date_rng = pd.date_range(start=start_date, periods=48, freq=frequency)

# Creating a DataFrame using the generated DatetimeIndex
df = pd.DataFrame(index=date_rng)
df['value'] = np.arange(48)

print(df)
