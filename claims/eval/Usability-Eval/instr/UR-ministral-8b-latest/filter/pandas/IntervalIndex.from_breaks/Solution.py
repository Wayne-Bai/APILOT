import pandas as pd

# Sample data for demonstration
splits = [10, 20, 30, 40, 50]

# Convert the array of splits to an IntervalIndex
interval_index = pd.IntervalIndex(intervals=[(min(splits)-1, max(splits))] + [(splits[i], splits[i+1]) for i in range(len(splits)-1)])

# Create a DataFrame with the IntervalIndex
dates = pd.date_range(start='2023-01-01', periods=len(interval_index), freq='D')
df = pd.DataFrame({'Date': dates, 'Value': range(len(intervals))})
df_buf = df.set_index('Date')
df_buf.index = interval_index

print(df_buf)
