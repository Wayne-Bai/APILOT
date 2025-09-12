import pandas as pd

# Assuming you have a DateTimeIndex and the new frequency
df = pd.Series(range(10), index=pd.date_range(start='1/1/2001', periods=10, freq='H'))
df.index = df.index.to_period('H')
df.index = df.index.asfreq('H')
