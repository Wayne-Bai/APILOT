import pandas as pd
from pandas import Series
import numpy as np

# Sample data
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Adding a string suffix to each column label
df.columns = [f"{col}_suffix" for col in df.columns]

# Display the DataFrame with updated column names
print(df)
