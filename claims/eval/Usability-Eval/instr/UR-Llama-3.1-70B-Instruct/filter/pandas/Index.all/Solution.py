import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': [True, False, True, True, True],
    'B': [True, True, True, True, True]
})

# Check if all elements are True in each column
print(df.all())

# Check if all elements are True in the entire DataFrame
print(df.values.all())

# Check if all elements are True in a Series
series = pd.Series([True, True, False, True])
print(series.all())
