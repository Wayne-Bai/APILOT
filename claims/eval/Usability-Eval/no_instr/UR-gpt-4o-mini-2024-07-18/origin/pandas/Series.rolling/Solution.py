import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data)

# Rolling window calculations
# Example: Calculate the rolling sum with a window size of 3
df['Rolling_Sum_A'] = df['A'].rolling(window=3).sum()
df['Rolling_Sum_B'] = df['B'].rolling(window=3).sum()

# Example: Calculate the rolling mean with a window size of 2
df['Rolling_Mean_A'] = df['A'].rolling(window=2).mean()
df['Rolling_Mean_B'] = df['B'].rolling(window=2).mean()

print(df)
