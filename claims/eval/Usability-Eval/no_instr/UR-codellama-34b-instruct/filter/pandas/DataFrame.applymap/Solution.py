
import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 42, 37],
        'grade': [80, 92, 75]}
df = pd.DataFrame(data)

# define the function to apply element-wise
def add_one(x):
    return x + 1

# apply the function element-wise using the .apply() method
result = df['age'].apply(add_one)
print(result)
