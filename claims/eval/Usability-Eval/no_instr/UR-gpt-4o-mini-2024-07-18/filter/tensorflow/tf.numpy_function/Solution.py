import tensorflow as tf

@tf.function
def my_custom_op(x):
    # Example operation, replace this with your actual logic
    return x * x + 2 * x + 1

# Create a TensorFlow constant for testing
input_tensor = tf.constant([1.0, 2.0, 3.0])

# Use the custom operation
output_tensor = my_custom_op(input_tensor)

print(output_tensor)
