import pandas as pd

# Sample data for demonstration
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

# Creating a DataFrame
df = pd.DataFrame(data)

# Resetting the index of the DataFrame
df_reset = df.reset_index(drop=True)

print(df_reset)
