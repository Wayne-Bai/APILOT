
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
 'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
 'Value': [1, 2, 3, 4, 5, 6]
})

# Group the dataframe by 'Group' and compute the sum of 'Value' for each group
grouped_df = df.groupby('Group')['Value'].sum()

# Print the result
print(grouped_df)
