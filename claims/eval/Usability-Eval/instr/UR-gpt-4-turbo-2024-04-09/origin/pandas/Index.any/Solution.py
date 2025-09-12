import pandas as pd

# Example DataFrame
data = {
    'A': [0, 0, 1, 0],
    'B': [False, False, True, False]
}
df = pd.DataFrame(data)

# Check whether any element in the DataFrame is True
result = df.any().any()

print(result)
