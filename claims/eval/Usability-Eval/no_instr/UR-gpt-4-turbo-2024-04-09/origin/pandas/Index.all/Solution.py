import pandas as pd

# Example dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 0],  # Contains a zero which is "Falsy"
    'C': [7, 8, 9]
})

# Check if all elements are Truthy
result = df.all().all()

print(result)
