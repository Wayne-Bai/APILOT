import pandas as pd

# define the left and right bounds arrays
left_bounds = [1, 2, 3, 4, 5]
right_bounds = [6, 7, 8, 9, 10]

# create a multi-index from the arrays
index = pd.MultiIndex.from_arrays([left_bounds, right_bounds], names=['Left', 'Right'])

# create a dataframe with the multi-index
df = pd.DataFrame(index=index)

# display the dataframe
print(df)
