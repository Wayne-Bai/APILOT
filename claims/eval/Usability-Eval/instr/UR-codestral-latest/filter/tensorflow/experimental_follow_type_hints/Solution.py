import tensorflow as tf

# Define a function with type annotations
def simple_operation(x: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
    # Perform an operation, like addition
    result = tf.add(x, y)
    return result

# Create some tensors
x = tf.constant([1, 2, 3])
y = tf.constant([4, 5, 6])

# Call the function
output = simple_operation(x, y)

# Print the result
print(output)
