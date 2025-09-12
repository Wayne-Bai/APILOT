
import pandas as pd

# Sample data frame
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 10, 20, 30, 40],
        'C': [100, 200, 300, 400, None]}

df = pd.DataFrame(data)

# Drop rows with missing values
df.dropna(inplace=True)

print(df)
