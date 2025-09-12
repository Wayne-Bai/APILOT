import pandas as pd

# Create a sample DataFrame
data = {
    'A': [True, False, 1, 0, 'hello', None, '', False],
    'B': [True, False, 4, 0, 'world', None, '', False],
    'C': [5, 6, 0, '', False, None, 'hello', '']
}
df = pd.DataFrame(data)

# Use the any() method with applymap() to check for any Truthy elements in the DataFrame
def is_truthy(value):
    return bool(value)

series = df.applymap(is_truthy)
result = series.any().any()

print(result)
