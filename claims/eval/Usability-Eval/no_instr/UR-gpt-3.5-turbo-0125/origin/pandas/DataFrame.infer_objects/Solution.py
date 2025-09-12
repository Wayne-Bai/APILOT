
import pandas as pd

# Load your dataset into a DataFrame, let's assume your DataFrame is named 'df'
df = pd.read_csv('your_dataset.csv')

# Attempt to infer better dtypes for object columns
df = df.infer_objects()

# Display the updated DataFrame with optimized dtypes
print(df.dtypes)
