import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Rolling window calculations
rolling_mean = df.rolling(window=3).mean()
rolling_sum = df.rolling(window=3).sum()
rolling_std = df.rolling(window=3).std()

print("Rolling Mean:")
print(rolling_mean)
print("\nRolling Sum:")
print(rolling_sum)
print("\nRolling Standard Deviation:")
print(rolling_std)
