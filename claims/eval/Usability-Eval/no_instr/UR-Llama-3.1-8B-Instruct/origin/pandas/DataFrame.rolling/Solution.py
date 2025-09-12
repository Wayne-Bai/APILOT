import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
index = pd.date_range('2022-01-01', periods=100, freq='D')
data = np.random.rand(100)
df = pd.DataFrame(data, index=index, columns=['Value'])

# Perform rolling window calculations with mean, sum, max, min, and std
df['Rolling Mean'] = df['Value'].rolling(window=10).mean()
df['Rolling Sum'] = df['Value'].rolling(window=10).sum()
df['Rolling Max'] = df['Value'].rolling(window=10).max()
df['Rolling Min'] = df['Value'].rolling(window=10).min()
df['Rolling Std'] = df['Value'].rolling(window=10).std()

# Backfill the NaN values
df['Rolling Mean'] = df['Rolling Mean'].fillna(method='backfill')
df['Rolling Sum'] = df['Rolling Sum'].fillna(method='backfill')
df['Rolling Max'] = df['Rolling Max'].fillna(method='backfill')
df['Rolling Min'] = df['Rolling Min'].fillna(method='backfill')
df['Rolling Std'] = df['Rolling Std'].fillna(method='backfill')

# Print the result
print(df.tail())
