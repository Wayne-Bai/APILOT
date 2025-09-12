
import pandas as pd

# load the csv file
df = pd.read_csv('data.csv')

# perform the reduction operation
result = df['value'].sum()

print(result)
