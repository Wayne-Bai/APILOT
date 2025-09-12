
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['apple', 'banana', 'cherry', 'date', 'elderberry']
})

quantile_value = 0.5

grouped = df.groupby('A')['A'].quantile(quantile_value)

print(grouped)
