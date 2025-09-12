# Import necessary libraries
import pandas as pd

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 12, 11, 18, 19, 15, 20, 22, float('nan')],
}
df = pd.DataFrame(data)

# Compute the standard error of the mean for each group, excluding missing values
semean = df.groupby('Group')['Value'].apply(lambda x: x_dropna().std() / x_dropna().count() * (1 / x_dropna().count() ** 0.5))

# Print the result
print(semean)
