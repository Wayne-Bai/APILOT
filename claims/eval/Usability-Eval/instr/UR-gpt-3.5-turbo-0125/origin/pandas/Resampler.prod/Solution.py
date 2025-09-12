
import pandas as pd

# Create a sample DataFrame
data = {'group': ['A', 'A', 'B', 'B'],
        'value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Calculate the product of group values
result = df.groupby('group')['value'].prod()

print(result)
