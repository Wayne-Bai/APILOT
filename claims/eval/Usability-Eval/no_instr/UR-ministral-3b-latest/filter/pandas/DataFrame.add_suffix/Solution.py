import pandas as pd

# Example data for demonstration
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

df = pd.DataFrame(data)

# Adding a new column with suffix to existing columns values
df = df.assign(dataset='original_data')

# Display the updated DataFrame
print(df)
