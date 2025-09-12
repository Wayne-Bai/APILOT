
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Print the original DataFrame
print(df)

# Reset the index of the DataFrame
df_reset = df.reset_index(drop=True)

# Print the DataFrame with the reset index
print(df_reset)
