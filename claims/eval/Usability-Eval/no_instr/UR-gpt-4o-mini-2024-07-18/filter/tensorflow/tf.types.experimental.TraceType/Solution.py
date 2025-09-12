import tensorflow as tf

# Define a simple function that takes in a tensor and performs an operation
@tf.function
def multiply_by_two(x: tf.Tensor) -> tf.Tensor:
    return x * 2

# Create a sample tensor
input_tensor = tf.constant([1, 2, 3, 4])

# Call the function and print the output
output_tensor = multiply_by_two(input_tensor)
print(output_tensor)
