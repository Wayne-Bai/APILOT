import pandas as pd

# Sample DataFrame creation for demonstration
data = {'Name': ['John', 'Anna', 'James', 'Linda'],
        'Age': [28, 22, 35, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Function to return the first n rows of the DataFrame
def get_first_n_rows(df, n):
    return df.head(n)

# Example usage to get the first 2 rows
result = get_first_n_rows(df, 2)
print(result)
