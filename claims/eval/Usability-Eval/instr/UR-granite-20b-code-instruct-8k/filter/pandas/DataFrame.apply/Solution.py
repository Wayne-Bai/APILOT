import pandas as pd
# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Apply a function along an axis of the DataFrame
result = df.apply(sum, axis=0)

# Output the result
print(result)
