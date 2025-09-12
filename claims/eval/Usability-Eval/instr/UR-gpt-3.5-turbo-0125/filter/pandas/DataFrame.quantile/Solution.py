
import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(data)

quantile_value = 0.5  # Example: 0.5 for median

result = df.quantile(q=quantile_value, axis=0)
print(result)
