
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace=True)

# Output the DataFrame with reset index
print(df)
