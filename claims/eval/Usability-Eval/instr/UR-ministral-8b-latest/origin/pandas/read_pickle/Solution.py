import pandas as pd

# Assuming the pickled file is named 'data.pkl'
df = pd.read_pickle('data.pkl')

# To explore the dataframe
print(df.head())

# To see the data types of the columns
print(df.dtypes)

# To get summary statistics
print(df.describe())
