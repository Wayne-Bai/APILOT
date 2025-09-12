
import pandas as pd

# Create a datetime index with a specified frequency
date_range = pd.date_range('20220101', '20220131', freq='D')

# Print the datetime index
print(date_range)

# Change the frequency to monthly
monthly_range = date_range.to_period('M')

# Print the monthly period range
print(monthly_range)

# Convert the monthly period range back to a datetime index
monthly_index = monthly_range.to_timestamp()

# Print the monthly datetime index
print(monthly_index)
