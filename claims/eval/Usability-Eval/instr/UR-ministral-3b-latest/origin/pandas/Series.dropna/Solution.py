import pandas as pd
# Assuming you have a CSV file called 'data.csv'
df = pd.read_csv('data.csv')
df = df.dropna()  # Removing rows with any missing values
