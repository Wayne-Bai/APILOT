
import pandas as pd

# Create a sample series
s = pd.Series([True, True, False])

# Check if all elements are truthy
if s.all():
    print("All elements are truthy")
else:
    print("Not all elements are truthy")
