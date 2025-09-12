import pandas as pd

# Define the frequency
freq = 'H'  # Hourly frequency

# Define the start and end dates
start_date = '2022-01-01 00:00:00'
end_date = '2022-01-02 00:00:00'

# Generate fixed frequency DatetimeIndex
index = pd.date_range(start=start_date, end=end_date, freq=freq)

# Convert the index to a DataFrame
df = pd.DataFrame(index=index)

# Display the first few rows of the DataFrame
df.head()
