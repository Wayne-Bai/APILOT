import pandas as pd

# Sample DataFrame creation for demonstration
data = {
    'A': range(1, 11),
    'B': range(11, 21)
}
df = pd.DataFrame(data)

# Function to return the last n rows
def get_last_n_rows(dataframe, n):
    return dataframe.tail(n)

# Example usage
n = 3  # Number of rows to return
last_n_rows = get_last_n_rows(df, n)
print(last_n_rows)
