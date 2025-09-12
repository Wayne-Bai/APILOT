import pandas as pd

# Define the data
data = pd.Series([True, False, True])

# Check if all elements are Truthy
all_truthy = data.all()

print(all_truthy)
