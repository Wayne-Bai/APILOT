import pandas as pd

# Generate a fixed frequency DatetimeIndex
# Specify start date, end date, and frequency
start_date = '2023-05-01'
end_date = '2023-05-10'
frequency = 'D'  # 'D' for daily frequency

# Create the DatetimeIndex
datetime_index = pd.date_range(start=start_date, end=end_date, freq=frequency)

# Display the DatetimeIndex
print(datetime_index)
