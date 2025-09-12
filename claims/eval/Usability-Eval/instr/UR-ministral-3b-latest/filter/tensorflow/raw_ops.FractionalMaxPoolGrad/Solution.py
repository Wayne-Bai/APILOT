import tensorflow as tf

# Assuming method to compute gradient of FractionalMaxPool function
def method(input_tensor, kernel_size, strides, padding='SAME'):
    # Compute FractionalMaxPool (and its gradient) using custom operations
    # This is a simplified example, a more sophisticated implementation is required
    pool_shape = tf.shape(input_tensor)[:2]  # Ignoring batch dimension
    kernel_height, kernel_width = kernel_size
    stride_height, stride_width = strides

    # Handle padding
    if padding == 'SAME':
        output_height = pool_shape[0] // stride_height
        output_width = pool_shape[1] // stride_width
    elif padding == 'VALID':
        output_height = (pool_shape[0] - 1) // stride_height
        output_width = (pool_shape[1] - 1) // stride_width

    pooled_output = tf.nn.fractional_max_pool(input_tensor, kernel_size, strides)

    # Apply output logic here
    # Terminating as this is a mock code

    return pooled_output

# Testing the method with some dummy data
input_tensor = tf.random.normal([1, 24, 24, 64], dtype=tf.float32)
kernel_size = (7, 7)
strides = (1, 1)

# Compute weights & bias for FractionalMaxPool gradient computation
weights = tf.Variable(tf.random.normal([1, kernel_size[0], kernel_size[1], 64], dtype=tf.float32))
bias = tf.Variable(tf.zeros([64], dtype=tf.float32))

# Define the forward pass for simplicity
output = method(input_tensor, kernel_size, strides)

# Compute the gradient
gradient = tf.gradients(output, [input_tensor], grad_outputs=tf.ones_like(output), outputs_gradients=[weights, bias])

print(gradient)
