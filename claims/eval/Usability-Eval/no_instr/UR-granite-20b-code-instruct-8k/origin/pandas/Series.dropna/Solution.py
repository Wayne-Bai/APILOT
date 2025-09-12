import pandas as pd

# read the csv file
df = pd.read_csv('filename.csv')

# remove missing values
df.dropna(inplace=True)

# write the updated dataframe to a new csv file
df.to_csv('updated_filename.csv', index=False)
