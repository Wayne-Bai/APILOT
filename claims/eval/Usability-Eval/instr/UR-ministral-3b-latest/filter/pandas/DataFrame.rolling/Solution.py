import pandas as pd

# Create a sample DataFrame
data = {
    'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'date': pd.date_range(start='2023-01-01', periods=10)
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Calculate rolling window with a specified window size and function
rolling_window = 3  # Example: rolling window of 3 days
df['rolling_mean'] = df['value'].rolling(window=rolling_window).mean()

print(df)
