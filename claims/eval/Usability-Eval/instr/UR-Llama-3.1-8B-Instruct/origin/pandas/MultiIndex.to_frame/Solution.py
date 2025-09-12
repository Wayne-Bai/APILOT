import pandas as pd

# Create a dictionary with data
data = {
    ('USA', 'New York'): {'Population': 20.2, 'Area': 328.23},
    ('USA', 'California'): {'Population': 39.5, 'Area': 163707.91},
    ('Canada', 'Toronto'): {'Population': 2.7, 'Area': 243.43},
    ('Canada', 'Montreal'): {'Population': 1.7, 'Area': 365.08}
}

# Create a DataFrame
df = pd.DataFrame(data).T

# Rename the columns to be the index levels
df.columns.name = 'Levels'

# Pivot the DataFrame to show the index levels as columns
print(df.stack().T)
