# Importing the necessary libraries
import pandas as pd

# Creating a sample DataFrame
data = {
    'Group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Printing the original DataFrame
print("Original DataFrame:")
print(df)

# Grouping by 'Group' and computing the product of 'Values'
grouped = df.groupby('Group')['Values'].prod().reset_index()

# Printing the result
print("\nProduct of 'Values' for each group:")
print(grouped)
