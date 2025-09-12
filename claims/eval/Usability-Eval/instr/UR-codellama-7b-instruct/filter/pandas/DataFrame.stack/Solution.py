
import pandas as pd

# load data from CSV file
data = pd.read_csv('data.csv')

# groupby and aggregate
result = data.groupby(['level1', 'level2'])['value'].agg({'mean': np.mean, 'std': np.std})

# output to CSV
result.to_csv('output.csv', index=True)
