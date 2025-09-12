import pandas as pd

# Assuming df is your DataFrame and 'data' is the column you want to perform the calculation on
df = pd.DataFrame({'data': [i for i in range(1, 101)]})

df['7_day_rolling_mean'] = df['data'].rolling(window=7).mean()

print(df.head(10))
