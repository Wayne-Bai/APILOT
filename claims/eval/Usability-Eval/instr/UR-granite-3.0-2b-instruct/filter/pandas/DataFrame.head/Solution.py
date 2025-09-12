import pandas as pd

# Assuming df is your DataFrame and n is the number of rows you want to return
n = 5
df = pd.read_csv('your_file.csv')  # replace 'your_file.csv' with your actual file path
df = df.head(n)
