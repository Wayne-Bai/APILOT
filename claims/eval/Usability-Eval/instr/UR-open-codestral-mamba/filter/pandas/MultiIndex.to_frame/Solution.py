import pandas as pd

# Assuming this is your data
data = {
    ('A', 'X'): [1, 2, 3, 4, 5],
    ('A', 'Y'): [6, 7, 8, 9, 10],
    ('B', 'X'): [11, 12, 13, 14, 15],
    ('B', 'Y'): [16, 17, 18, 19, 20]
}

# Create the DataFrame using DataFrame constructor
df = pd.DataFrame(data, columns=pd.MultiIndex.from_tuples([(a,b) for a,b in data.keys()]))

# Set the column levels as DataFrame columns
df.columns = df.columns.to_flat_index()
