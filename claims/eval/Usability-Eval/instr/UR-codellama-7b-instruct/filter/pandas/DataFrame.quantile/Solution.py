import pandas as pd

# Read in data from a file
data = pd.read_csv('data.csv')

# Calculate the median value for column 'x'
median_x = data['x'].quantile(0.5)

# Calculate the median value for column 'y'
median_y = data['y'].quantile(0.5)
