import pandas as pd

# Load your dataset
# df = pd.read_csv('your_dataset.csv')

# Infer better dtypes for object columns
df['column_name'] = df['column_name'].astype('infer')

# Print the data types of the object columns
print(df.dtypes)
