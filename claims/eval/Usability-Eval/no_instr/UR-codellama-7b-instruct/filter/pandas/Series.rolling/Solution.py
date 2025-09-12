
import pandas as pd

# create a sample dataframe
data = {'timestamp': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05'],
        'value': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# define the rolling window calculation
window_size = 2
df['rolling_mean'] = df['value'].rolling(window=window_size).mean()
