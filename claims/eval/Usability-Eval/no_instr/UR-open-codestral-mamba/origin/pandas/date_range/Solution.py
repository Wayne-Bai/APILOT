import pandas as pd

start_date = '2022-01-01'
end_date = '2022-01-31'
freq = 'D'  # daily frequency

# Create a date range
date_range = pd.date_range(start=start_date, end=end_date, freq=freq)

print(date_range)
