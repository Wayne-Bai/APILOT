import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Perform a reduction operation, such as summing all elements in the DataFrame
scalar_result = df.to_numpy().sum()

print("Scalar result of reduction operation:", scalar_result)
