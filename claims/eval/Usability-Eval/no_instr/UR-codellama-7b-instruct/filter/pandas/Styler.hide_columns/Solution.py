
import pandas as pd

# Load data from CSV file
data = pd.read_csv('data.csv')

# Drop the first row (header)
data.drop(index=0, axis=0, inplace=True)

# Rename the columns with a new name and create a new dataframe
new_df = data.rename(columns={'old_col1': 'new_col1', 'old_col2': 'new_col2'})

# Save the dataframe to a CSV file
new_df.to_csv('data_modified.csv', index=False)
