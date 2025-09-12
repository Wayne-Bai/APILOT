
import pandas as pd

# Create a sample DataFrame with mixed data types
df = pd.DataFrame({'A': [1, 'a', True], 'B': [2, 'b', False]})

# Check if all elements in the DataFrame are truthy
print(df.all())  # Output: True

# Check if all elements in a specific column are truthy
print(df['A'].all())  # Output: True
