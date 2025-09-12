# Import the pandas library
import pandas as pd

# Generate a date range with a frequency of 1 hour
date_range = pd.date_range(start='1/1/2024', periods=10, freq='H')

# Print the date range
print(date_range)
