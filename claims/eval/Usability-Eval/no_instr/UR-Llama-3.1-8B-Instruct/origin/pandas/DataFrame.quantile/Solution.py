import pandas as pd

# Let's create a DataFrame with random data for demonstration purposes
# We'll use numpy to generate random values for our DataFrame
import numpy as np

data = np.random.randint(0, 100, size=(5, 4))
df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(1, 5)])

print("Original DataFrame:")
print(df)

# Now, let's calculate the quantile of the values in each column (default axis is columns, if not specified)
quantile_75 = df.quantile(0.75)

print("\nQuantile of 0.75 (75%) over the columns:")
print(quantile_75)

# If you want to calculate the quantile over rows instead of columns, specify the axis argument
quantile_50_over_rows = df.quantile(0.5, axis=1)

print("\nQuantile of 0.5 (50%) over the rows:")
print(quantile_50_over_rows)
