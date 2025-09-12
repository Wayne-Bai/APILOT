import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Get the index of the first occurrence of the maximum value in the DataFrame
# along the specified axis
max_value = df.max().max()  # get the max value in the DataFrame
max_index = df.loc[df[df['A'] == max_value].index[0]].to_dict()  # Get Column Index 
ids = []
for key, value in max_index.items():
    if key == 'A' or key == 'B':
        ids.append(value)
index_first_maxover_row = df.loc[df['A'] == df['A'].max()].index[0]  # get the first occurrence of maximum value
index_first_maxover_col = df.loc[index_first_maxover_row].idxmax()  # get the index of the column which is max 

# Print the result
print("\nIndex of the first occurrence of the maximum value:")
print(f"First Index along specified axis: {index_first_maxover_row}")
print(f"Second Index along specified axis: {index_first_maxover_col}")
