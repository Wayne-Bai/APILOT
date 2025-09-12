# Import pandas library
import pandas as pd

# Create a DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Perform reduction operation (sum) without using the sum API
result = df['A'].reduce(lambda x, y: x + y)

print(result)
