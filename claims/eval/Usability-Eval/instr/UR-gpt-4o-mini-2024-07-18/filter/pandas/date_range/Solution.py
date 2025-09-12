import pandas as pd

# Create a fixed frequency DatetimeIndex
start_date = '2023-01-01'
end_date = '2023-01-10'
freq = 'D'  # Daily frequency

# Generate the DatetimeIndex
date_index = pd.date_range(start=start_date, end=end_date, freq=freq)

print(date_index)
