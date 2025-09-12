
import pandas as pd

# create sample data
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'grade': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# define custom function to apply along axis
def my_func(x):
    return x + 1

# apply custom function along axis 0 (rows)
df['age_plus_one'] = df['age'].apply(my_func, axis=0)

print(df)
