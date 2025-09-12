import pandas as pd

# assuming df is your DataFrame
df = pd.read_csv('your_file.csv')  # replace 'your_file.csv' with the path to your file

# attempt to infer better dtypes for object columns
df = df.convert_dtypes()

print(df.dtypes)
