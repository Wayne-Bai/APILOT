import pandas as pd

# Sample DataFrame
data = {
    'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)

# Rolling window calculation (e.g., rolling mean with a window size of 3)
df['rolling_mean'] = df['value'].rolling(window=3, min_periods=1).mean()

print(df)
