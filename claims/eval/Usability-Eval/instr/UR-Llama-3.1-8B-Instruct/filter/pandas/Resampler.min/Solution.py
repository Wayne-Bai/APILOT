# Importing the pandas library
import pandas as pd

# Create a DataFrame (replace this with your actual data)
data = {'Name': ['Tom', 'Nick', 'Tom', 'John', 'John', 'John'],
        'Age': [20, 21, 19, 18, 20, 22],
        'Score': [90, 85, 88, 92, 89, 95]}
df = pd.DataFrame(data)

# Group by 'Name' and compute the minimum value for 'Age' and 'Score'
min_age = df.groupby('Name')['Age'].min()
min_score = df.groupby('Name')['Score'].min()

print('Minimum Age:', min_age)
print('Minimum Score:', min_score)
