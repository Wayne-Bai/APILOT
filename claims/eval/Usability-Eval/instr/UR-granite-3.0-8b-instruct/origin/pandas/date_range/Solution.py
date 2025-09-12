import pandas as pd

# Define the start and end dates
start_date = '2022-01-01'
end_date = '2022-12-31'

# Define the frequency (e.g., 'D' for daily, 'M' for monthly, 'Y' for yearly)
frequency = 'D'

# Create a DatetimeIndex with the specified frequency
date_range = pd.date_range(start=start_date, end=end_date, freq=frequency)

# Create a DataFrame with the DatetimeIndex
df = pd.DataFrame(index=date_range)
