
import pandas as pd

# Load the data into a pandas dataframe
df = pd.read_csv('data.csv')

# Resample the data at 1 minute frequency
df_resampled = df.resample('1T').mean()

# Output the resampled data to a new csv file
df_resampled.to_csv('output.csv', index=False)
