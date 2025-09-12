import pandas as pd

# Sample data
data = {'Date': pd.date_range(start='1/1/2022', periods=10),
        'Sales': [100, 150, 140, 170, 190, 210, 230, 250, 270, 290]}
df = pd.DataFrame(data)

# Set 'Date' column as the index
df.set_index('Date', inplace=True)

# Perform a rolling mean calculation with a window of 3
df['Rolling_Mean'] = df['Sales'].rolling(window=3).mean()

print(df)
