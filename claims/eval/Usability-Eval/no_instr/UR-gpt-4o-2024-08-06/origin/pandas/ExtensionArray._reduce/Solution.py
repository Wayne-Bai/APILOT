import pandas as pd

# Sample DataFrame
data = {
    'values': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Reduction operation example: calculate the sum of the 'values' column
scalar_result = df['values'].sum()

print(scalar_result)  # Output: 150
