import pandas as pd

# Assuming df is your DataFrame and it has object columns
# First, let's check the current dtypes
print("Current dtypes:")
print(df.dtypes)

# We can infer better dtypes using the infer_objects function
df = df.infer_objects()

# Let's check the updated dtypes
print("\nUpdated dtypes:")
print(df.dtypes)
