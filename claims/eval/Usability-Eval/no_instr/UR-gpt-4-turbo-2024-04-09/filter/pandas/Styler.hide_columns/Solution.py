import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Job': ['Engineer', 'Doctor', 'Artist']}
df = pd.DataFrame(data)

# Method to print DataFrame without column headers
print(df.to_string(index=False, header=False))
