
import pandas as pd

# Load the data from the CSV file into a Pandas dataframe
df = pd.read_csv('data.csv')

# Perform the reduction operation on the 'value' column
result = df['value'].sum()

print(result)
