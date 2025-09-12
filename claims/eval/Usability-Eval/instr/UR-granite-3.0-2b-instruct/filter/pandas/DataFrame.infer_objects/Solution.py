import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv('your_file.csv')

# Infer better dtypes for object columns
df = df.infer_objects()

# Print the updated DataFrame
print(df.dtypes)
