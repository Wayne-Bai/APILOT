import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Performing a reduction operation (e.g., sum of all elements)
scalar_result = df.sum().sum()

print(scalar_result)
