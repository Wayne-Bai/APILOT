import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [True, False, True]
}
df = pd.DataFrame(data)

# Convert the DataFrame to a dictionary
dict_output = df.to_dict(orient='records')

print(dict_output)
