# Import the necessary pandas library
import pandas as pd

# Define a dictionary containing data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Value': [10, 20, 30, 40, 50]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the number of rows to return
n = 2

# Select the last n rows
last_n_rows = df.iloc[-n:]

# Print the result
print(last_n_rows)
