import pandas as pd

# Load the data into a pandas dataframe
# df = pd.read_csv('your_data.csv')

# Return the last 10 rows
last_10_rows = df.tail(10)

# Or return the last n rows, replace n with your desired number
last_n_rows = df.tail(n)
