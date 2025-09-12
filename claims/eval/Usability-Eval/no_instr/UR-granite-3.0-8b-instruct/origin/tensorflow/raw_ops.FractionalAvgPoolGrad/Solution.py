import tensorflow as tf

# Define the input tensor
input_tensor = tf.placeholder(tf.float32, shape=[None, height, width, channels])

# Define the pool size
pool_size = [pool_height, pool_width]

# Define the padding type
padding = 'VALID'  # or 'SAME'

# Compute the gradient of the FractionalAvgPool function
grad = tf.raw_ops.FractionalAvgPoolGrad(input_tensor, pool_size, padding)

# Print the gradient tensor
print(grad)
