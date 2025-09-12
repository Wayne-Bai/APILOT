# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Compute max value of group
max_value = df.groupby('Category')['Value'].max()

# Print the result
print(max_value)
