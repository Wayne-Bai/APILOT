import tensorflow as tf

# Define a function to apply to each element
def apply_fn(x):
    # Your function logic here
    return x * 2

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Apply the function to each element
result = tf.map_fn(apply_fn, tensor)

# Print the result
print(result)
