
import pandas as pd

# Load the dataframe
df = pd.read_csv("data.csv")

# Infer better dtypes for object columns
df = df.infer_objects()

# Print the updated data types
print(df.dtypes)
