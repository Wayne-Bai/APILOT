# Importing pandas
import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': ['a', 'b', 'c'],
    'B': [1, 2, 3],
    'C': [1.1, 2.2, 3.3]
})

# To infer better dtypes for object columns
df = df.convert_dtypes()

print(df.dtypes)
