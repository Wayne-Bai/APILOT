import pandas as pd

# Assuming the csv file named 'data.csv' in the same directory as your python script

# Read CSV file into DataFrame
data = pd.read_csv('data.csv')

# Convert DataFrame to numpy array
array_data = data.to_numpy()

# Print array content
print(array_data)
