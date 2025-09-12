# Importing necessary libraries
import pandas as pd
import numpy as np

# Creating a DataFrame for demonstration
np.random.seed(0)
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': ['small', 'large', 'large','small','small', 'large','small', 'large'],
    'D': np.random.randint(1, 100, 8),
    'E': np.random.randn(8)
})

# Using groupby and quantile function
print("Original DataFrame:")
print(df)

group_quantile = df.groupby('A')['D'].quantile(0.75)

print("\nReturn group values at the given quantile:")
print(group_quantile)

# Applying quantile to each column
print("\nApply quantile to each column:")
print(df.groupby('A').quantile(0.75))

# Applying different quantiles to different columns
print("\nApply different quantiles to different columns:")
quantiles = df.groupby('A').agg({'D': lambda x: x.quantile(0.75), 'E': lambda x: x.quantile(0.25)})

print(quantiles)
