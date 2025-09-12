import pandas as pd

# generate a fixed frequency DatetimeIndex
start_date = '2023-01-01'
end_date = '2023-12-31'
freq = 'M'  # for monthly frequency

date_range = pd.date_range(start_date, end_date, freq=freq)
