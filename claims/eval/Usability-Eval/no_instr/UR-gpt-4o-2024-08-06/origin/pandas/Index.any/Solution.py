import pandas as pd

# Create a sample pandas Series
data = pd.Series([0, '', None, False, 5])

# Check if any element is truthy
any_truthy = data.astype(bool).any()

print(any_truthy)
