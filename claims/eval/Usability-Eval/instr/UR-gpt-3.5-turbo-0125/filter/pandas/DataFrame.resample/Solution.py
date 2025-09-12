
import pandas as pd

# Create a sample time series data
data = {'date': pd.date_range(start='1/1/2022', periods=100, freq='D'),
        'value': range(100)}
df = pd.DataFrame(data)

# Resample the time series data to monthly frequency
df_resampled = df.set_index('date').resample('M').sum()

print(df_resampled)
