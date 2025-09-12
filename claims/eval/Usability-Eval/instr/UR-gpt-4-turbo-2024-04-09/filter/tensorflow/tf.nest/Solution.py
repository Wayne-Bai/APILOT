import tensorflow as tf

# Example using tf.nest.map_structure
def multiply_by_two(x):
    return x * 2

# Define a nested structure
nested_list = [[1, 2], [3, 4, 5]]

# Applying the function to each element in the nested structure
result = tf.nest.map_structure(multiply_by_two, nested_list)

print("Original structure:", nested_list)
print("After applying function:", result)
