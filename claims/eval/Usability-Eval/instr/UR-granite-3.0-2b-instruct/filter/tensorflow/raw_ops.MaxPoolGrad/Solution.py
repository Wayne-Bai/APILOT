import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the max pooling parameters
pool_height = 2
pool_width = 2
strides = [1, 1, 1, 1]

# Create the max pooling operation
max_pooling_op = tf.raw_ops.MaxPoolGrad(
    input=input_tensor,
    pool_height=pool_height,
    pool_width=pool_width,
    strides=strides,
    dilations=[1, 1, 1, 1],
    data_format='NHWC',
    name='max_pooling_grad'
)

# Compute the gradients
gradients = tf.reshape(max_pooling_op, (-1,))

# Print the gradients
print(gradients)
