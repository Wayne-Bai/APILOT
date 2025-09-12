import tensorflow as tf

# Define the input tensor and the pooling parameters
input_tensor = tf.constant([[[[1.0], [2.0]],
                             [[3.0], [4.0]]]], dtype=tf.float32)

# Define the gradient tensor (e.g., gradient from the next layer in the network)
# For simplification, let's assume it's a tensor with the same shape as the output of the max pooling
grad = tf.constant([[[[1.0], [0.0]]]], dtype=tf.float32)

# Define pooling size and strides
pool_size = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
padding = 'VALID'

# Apply max pooling
with tf.GradientTape(persistent=True) as tape:
    tape.watch(input_tensor)
    pooled_output = tf.nn.max_pool2d(input_tensor, ksize=pool_size, strides=strides, padding=padding)

# Compute gradients of the max pooling
gradients = tape.gradient(pooled_output, input_tensor, output_gradients=grad)

# Print the gradients to verify
print("Gradients:\n", gradients)
