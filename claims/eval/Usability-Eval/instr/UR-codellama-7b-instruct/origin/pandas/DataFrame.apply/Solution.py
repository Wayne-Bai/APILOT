
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})

# Apply a function along an axis of the DataFrame
result = df.apply(lambda x: x**2, axis=0)

print(result)
