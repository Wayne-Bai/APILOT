
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Replace all missing values in the "age" column with the mean of the remaining non-missing values
mean_age = df['age'].fillna(value=df['age'].mean())

# Write the updated DataFrame back to a CSV file
df.to_csv('updated_data.csv', index=False)
