import pandas as pd
import numpy as np

# Assume we have a DataFrame 'df'
# with columns 'A', 'B', 'C', 'D', 'E'

df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50),
    'C': np.random.rand(50),
    'D': np.random.rand(50),
    'E': np.random.rand(50)
})

# Implementing a 5 point rolling mean
df['A_rolling_mean'] = df['A'].rolling(window=5).mean()

df.head(10)
