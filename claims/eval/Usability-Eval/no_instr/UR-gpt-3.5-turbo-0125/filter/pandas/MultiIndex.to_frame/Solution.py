
import pandas as pd

# Create a sample data
data = {
    ('A', 'X'): [1, 2, 3],
    ('A', 'Y'): [4, 5, 6],
    ('B', 'X'): [7, 8, 9],
    ('B', 'Y'): [10, 11, 12]
}

# Create a DataFrame with MultiIndex as columns
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
