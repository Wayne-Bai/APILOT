
import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv('dataset.csv')

# Remove missing values
df.dropna(inplace=True)

# Print the updated DataFrame
print(df)
