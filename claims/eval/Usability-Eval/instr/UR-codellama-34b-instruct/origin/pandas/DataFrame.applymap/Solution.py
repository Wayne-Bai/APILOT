
import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# define a function to apply to each element in the dataframe
def square_age(x):
    return x['age'] ** 2

# use the apply method to apply the function to each row in the dataframe
result = df.apply(square_age, axis=1)
print(result)
