
import pandas as pd

# create a sample series with different values
series = pd.Series([True, False, None, "hello", 0])

# use the any() function to check if any value is truthy
print(series.any()) # prints True
