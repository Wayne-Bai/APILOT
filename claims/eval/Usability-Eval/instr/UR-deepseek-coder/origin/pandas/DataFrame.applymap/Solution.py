import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Function to apply elementwise
def square(x):
    return x ** 2

# Applying the function elementwise
df = df.applymap(square)

print(df)
