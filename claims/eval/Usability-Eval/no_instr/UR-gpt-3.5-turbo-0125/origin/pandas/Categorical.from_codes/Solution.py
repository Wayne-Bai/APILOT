
import pandas as pd

# Creating a DataFrame
data = {'Codes': [1, 2, 1, 3, 2, 3], 'Categories': ['A', 'B', 'A', 'C', 'B', 'C']}
df = pd.DataFrame(data)

# Creating a Categorical type from codes and categories
df['Categories'] = pd.Categorical(df['Categories'], categories=['A', 'B', 'C'])

print(df['Categories'])
