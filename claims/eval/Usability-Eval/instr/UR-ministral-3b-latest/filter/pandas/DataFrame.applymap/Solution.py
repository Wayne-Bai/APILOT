import pandas as pd

# Assuming the DataFrame 'df' is already created
def apply_function(element):
    # Example function
    return element * 2  # Multiplying an element by 2

# Applying the function to the DataFrame element-wise
df_processed = df.applymap(apply_function)

print(df_processed)
