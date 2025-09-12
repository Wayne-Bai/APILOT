# Import the pandas library
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'Age': [28, 24, 35, 32, 40],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Function to return the first n rows of the DataFrame
def get_first_n_rows(df, n):
    return df.head(n)

# Use the function to get the first 3 rows
n = 3
print(get_first_n_rows(df, n))
