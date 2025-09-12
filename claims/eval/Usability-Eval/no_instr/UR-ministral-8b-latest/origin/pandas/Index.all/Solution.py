import pandas as pd

# Sample data
data = {'column1': [True, False, True], 'column2': [True, True, False]}

# Creating a DataFrame
df = pd.DataFrame(data)

# Check if all elements are Truthy
result = df.applymap(lambda x: x).all().all()

result
