import pandas as pd

# Assuming df is your DataFrame
def custom_function(x):
    # Your custom function logic goes here
    return x.mean()

# Applying the custom function along axis=0 (columns)
df_result = df.apply(custom_function, axis=0)

# Applying the custom function along axis=1 (rows)
df_result = df.apply(custom_function, axis=1)
