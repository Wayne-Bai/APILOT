import tensorflow as tf

# Define the input and bias tensors
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float16)
bias_tensor = tf.constant([4.0, 5.0, 6.0], dtype=tf.float16)

# Add the bias to the input tensor using the 'add' method
add_result = input_tensor + bias_tensor

# Print the result
print(add_result)
