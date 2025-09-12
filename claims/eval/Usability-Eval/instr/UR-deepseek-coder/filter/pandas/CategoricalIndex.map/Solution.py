import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': ['apple', 'banana', 'cherry', 'date']
}
df = pd.DataFrame(data)

# Example mapping dictionary
mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# Map values in column 'A' using the mapping dictionary
df['A'] = df['A'].map(mapping)

# Example function to map values in column 'B'
def map_fruit(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'cherry':
        return 'red'
    elif fruit == 'date':
        return 'brown'
    else:
        return 'unknown'

# Map values in column 'B' using the function
df['B'] = df['B'].map(map_fruit)

print(df)
