import pandas as pd

# Example data
data = {
    'date': pd.date_range('1/1/2023', periods=10, freq='D'),
    'value': range(10)
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Roll window calculation (e.g., 3-day moving average)
rolling_window = 3
df['rolling_mean'] = df['value'].rolling(window=rolling_window, min_periods=1).mean()

print(df)
