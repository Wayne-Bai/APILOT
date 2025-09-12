import pandas as pd

# Sample DataFrame creation
data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data)

# To prevent the display of the index, you can reset it and drop it.
df_no_index = df.reset_index(drop=True)

# Displaying the DataFrame without the index
print(df_no_index)
