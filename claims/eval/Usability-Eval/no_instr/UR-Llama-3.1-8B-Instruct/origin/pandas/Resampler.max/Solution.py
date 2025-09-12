# Importing pandas library
import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'Age': [28, 24, 35, 32, 40],
    'Score': [90, 85, 95, 92, 89]
}
df = pd.DataFrame(data)

# Grouping by 'Age' and computing max 'Score'
max_score_by_age = df.groupby('Age')['Score'].max()

# Printing the result
print(max_score_by_age)
