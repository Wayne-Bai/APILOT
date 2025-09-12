
import pandas as pd

# Sample DataFrame
data = {
    'values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)

# Rolling window calculations (e.g., rolling mean with a window size of 3)
df['rolling_mean'] = df['values'].rolling(window=3).mean()

# Display the DataFrame with the rolling mean
print(df)
