
# Importing pandas library
import pandas as pd

# Create a sample dataframe
data = {'A': ['1', '2', '3'],
        'B': ['x', 'y', 'z'],
        'C': ['True', 'False', 'True']}
df = pd.DataFrame(data)

# Infer better dtypes for object columns
for col in df.select_dtypes(include='object'):
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        pass

# Display the dataframe with inferred dtypes
print(df.dtypes)
