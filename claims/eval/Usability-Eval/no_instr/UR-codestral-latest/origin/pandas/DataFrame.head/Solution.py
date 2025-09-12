import pandas as pd

# Load a DataFrame (in this case, I'm loading from a CSV file as an example)
df = pd.read_csv('your_file.csv')

# Replace 'n' with the number of rows you want to return
n = 5

# Use the head() function to return the first 'n' rows
result = df.head(n)
