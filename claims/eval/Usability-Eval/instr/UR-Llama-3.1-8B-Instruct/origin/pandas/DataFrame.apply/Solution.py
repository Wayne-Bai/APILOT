# Import required libraries
import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Define a function to apply along the axis
def square(x):
    return x ** 2

# Apply the function along axis 0 (rows)
result_axis_0 = df.apply(square, axis=0)
print("Result applying function along axis 0 (rows):")
print(result_axis_0)

# Apply the function along axis 1 (columns)
result_axis_1 = df.apply(square, axis=1)
print("\nResult applying function along axis 1 (columns):")
print(result_axis_1)
