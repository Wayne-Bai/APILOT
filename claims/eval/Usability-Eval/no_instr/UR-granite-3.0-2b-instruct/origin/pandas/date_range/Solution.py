import pandas as pd

# Create a DataFrame with a datetime column
df = pd.DataFrame({
    'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']
})

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Set the 'date' column as the index with a fixed frequency (e.g., daily)
df.set_index('date', inplace=True, freq='D')
