import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the max pooling parameters
pool_size = (2, 2)
strides = (2, 2)
padding = 'VALID'

# Compute the gradients of the max pooling function
with tf.GradientTape() as tape:
    # Apply the max pooling operation
    output = tf.raw_ops.MaxPool(input=input_tensor, window_shape=pool_size, strides=strides, padding=padding)

# Compute the gradients
gradients = tape.gradient(output, input_tensor)

# Print the gradients
print(gradients)
