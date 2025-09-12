
import pandas as pd

# assuming the DataFrame 'df' contains the data and column 'ColA' is the column of interest
df = pd.DataFrame({
    'ColA': [1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, np.nan, 11],
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B'],
})

# Using groupby and std() function to calculate standard deviation of groups, excluding missing values
std_dev = df.groupby('Group')['ColA'].apply(lambda group: group.dropna().std())
print(std_dev)
