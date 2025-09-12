import pandas as pd

# Create a DataFrame
data = {
  'Name': ['Tom', 'Nick', 'John', 'Peter', 'Clark'],
  'Age': [20, 21, 19, 18, 22],
  'Score': [90, 85, 88, 92, 89]
}
df = pd.DataFrame(data)

# Return the first n rows
n = 3  # specify the number of rows
print(df.head(n))  # print the first n rows
