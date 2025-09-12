# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
}
df = pd.DataFrame(data)

# Define a function to be applied element-wise
def square(x):
    return x ** 2

# Apply the function element-wise using the map function
df_square = df.map(square)

# Alternatively, use the apply function with axis=0 to apply to each column
# or axis=1 to apply to each row
df_square_apply = df.applymap(square)

# Print the original DataFrame and the resulting DataFrame
print("Original DataFrame:")
print(df)
print("\nResulting DataFrame (using map function):")
print(df_square)
print("\nResulting DataFrame (using apply function with map equivalent):")
print(df_square_apply)
