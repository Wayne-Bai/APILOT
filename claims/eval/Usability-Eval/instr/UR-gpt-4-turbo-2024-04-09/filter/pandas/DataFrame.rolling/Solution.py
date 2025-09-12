import pandas as pd

# Sample data frame creation
data = {'values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Rolling window calculation (e.g., 3 periods rolling sum)
rolling_window_size = 3
df['rolling_sum'] = df['values'].rolling(window=rolling_window_size).sum()

print(df)
