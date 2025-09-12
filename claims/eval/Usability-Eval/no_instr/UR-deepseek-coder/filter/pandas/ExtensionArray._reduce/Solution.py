import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Performing a reduction operation (e.g., sum) and returning a scalar result
scalar_result = df['A'].sum()

print(scalar_result)
