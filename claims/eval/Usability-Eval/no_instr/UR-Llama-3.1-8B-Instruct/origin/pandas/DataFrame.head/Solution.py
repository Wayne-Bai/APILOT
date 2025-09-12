import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Mike'],
    'Age': [28, 24, 35, 32, 40],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Function to return the first n rows
def get_first_n_rows(df, n):
    return df.head(n)

# Test the function
n = 3  # number of rows to return
result = get_first_n_rows(df, n)

# Print the result
print("\nFirst {} rows:".format(n))
print(result)
