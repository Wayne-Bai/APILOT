import pandas as pd

# Load the dataset
data = pd.read_csv('data.csv')

# Set the index column
data.set_index(['level1', 'level2'], inplace=True)
