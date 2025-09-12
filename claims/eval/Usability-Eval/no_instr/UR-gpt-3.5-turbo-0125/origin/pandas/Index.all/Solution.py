
import pandas as pd

# Create a pandas Series with some elements
data = [True, False, True, True]
s = pd.Series(data)

# Check if all elements are Truthy
result = s.all()
print(result)
