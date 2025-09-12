import pandas as pd

# Create a DatetimeIndex with a specific start date and a specific frequency
start_date = '2022-01-01'
freq = 'D'  # daily frequency
index = pd.date_range(start=start_date, periods=10, freq=freq)

# Print the DatetimeIndex
print(index)

# Create a DatetimeIndex with a specific start date, a frequency 'Q' (quarterly) and quarters are not shifted when going back in time, using end='2022-01-01'
index_quarterly = pd.date_range('20220101', periods=10, frequencies='QS-JAN', end='2022-01-01')

# Print the DatetimeIndex
print(index_quarterly)
