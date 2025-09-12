import pandas as pd
import numpy as np

# Create a sample DataFrame
np.random.seed(0)
df = pd.DataFrame({
    'A': np.random.randint(1, 10, 10),
    'B': np.random.randint(1, 10, 10)
})

# Define a rolling window size
window_size = 3

# Apply rolling window calculations
df['Rolling_Sum_A'] = df['A'].rolling(window_size).sum()
df['Rolling_Mean_A'] = df['A'].rolling(window_size).mean()
df['Rolling.Std_A'] = df['A'].rolling(window_size).std()
df['Rolling_Min_A'] = df['A'].rolling(window_size).min()
df['Rolling_Max_A'] = df['A'].rolling(window_size).max()
df['Rolling_Var_A'] = df['A'].rolling(window_size).var()

print(df)
