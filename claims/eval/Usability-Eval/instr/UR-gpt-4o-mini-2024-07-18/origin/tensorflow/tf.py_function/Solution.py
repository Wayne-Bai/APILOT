import tensorflow as tf

@tf.function
def wrapped_function(x):
    # This is an example operation
    return x * x + 2 * x + 1

# Example usage
input_tensor = tf.constant([1, 2, 3, 4])
output_tensor = wrapped_function(input_tensor)

print(output_tensor.numpy())
