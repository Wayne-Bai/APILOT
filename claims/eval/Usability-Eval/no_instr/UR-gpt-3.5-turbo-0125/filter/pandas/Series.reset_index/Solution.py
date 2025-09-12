
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# Reset the index of the DataFrame
new_df = df.reset_index(drop=True)

print(new_df)
