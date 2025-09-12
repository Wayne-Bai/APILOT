
import pandas as pd

start_date = '2022-01-01'
end_date = '2022-01-10'
frequency = '1D'

date_index = pd.date_range(start=start_date, end=end_date, freq=frequency)

print(date_index)
