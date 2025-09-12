import pandas as pd

# Creating a dictionary with data
data = {
    ('A', 'a'): 1,
    ('A', 'b'): 2,
    ('B', 'a'): 3,
    ('B', 'b'): 4,
    ('C', 'a'): 5,
    ('C', 'b'): 6
}

# Creating a MultiIndex DataFrame
df = pd.DataFrame(data, columns=['A', 'C', 'B'])

# Resetting the index to move the levels to columns
df = df.reset_index()

# Renaming the columns
df = df.rename(columns={'level_0': 'B', 'level_1': 'A'})

# Sorting the levels enusre correct order 
df = df.sort_values(by='A')

print(df)
