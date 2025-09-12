import pandas as pd

# Sample data
data = {'Date': pd.date_range(start='1/1/2022', periods=10, freq='D'),
        'Value': [10, 15, 7, 30, 45, 25, 18, 30, 27, 15]}

df = pd.DataFrame(data)

# Rolling window calculations
df['Moving_Avg'] = df['Value'].rolling(window=3).mean()
df['Rolling_Sum'] = df['Value'].rolling(window=3).sum()

print(df)
