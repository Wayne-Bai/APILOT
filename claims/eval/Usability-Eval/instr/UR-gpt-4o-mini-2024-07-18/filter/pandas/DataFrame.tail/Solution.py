import pandas as pd

# Example DataFrame
data = {
    'A': range(10),
    'B': range(10, 20)
}
df = pd.DataFrame(data)

# Function to return the last n rows
def get_last_n_rows(dataframe, n):
    return dataframe.tail(n)

# Usage example
last_n_rows = get_last_n_rows(df, 3)
print(last_n_rows)
