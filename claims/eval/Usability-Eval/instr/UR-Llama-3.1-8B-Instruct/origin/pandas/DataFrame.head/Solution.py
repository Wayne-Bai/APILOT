# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
  "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "George"],
  "Age": [25, 30, 35, 40, 45, 50, 55],
  "Country": ["USA", "UK", "Australia", "Germany", "France", "Italy", "Spain"]
}
df = pd.DataFrame(data)

# Define the number of rows to return
n = 3

# Return the first n rows
print(df.head(n))
