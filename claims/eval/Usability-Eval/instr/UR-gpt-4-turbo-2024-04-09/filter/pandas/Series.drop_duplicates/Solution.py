import pandas as pd

# Sample data
data = {'values': [1, 2, 2, 3, 4, 4, 4, 5]}

# Create DataFrame
df = pd.DataFrame(data)

# Return Series with duplicate values removed
result_series = df['values'].drop_duplicates(keep=False)

# Display the result
print(result_series)
