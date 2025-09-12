import pandas as pd

# Generate a fixed frequency DatetimeIndex
start_date = '2023-01-01'
end_date = '2023-01-10'
frequency = 'D'  # Daily frequency

date_range = pd.date_range(start=start_date, end=end_date, freq=frequency)
print(date_range)
