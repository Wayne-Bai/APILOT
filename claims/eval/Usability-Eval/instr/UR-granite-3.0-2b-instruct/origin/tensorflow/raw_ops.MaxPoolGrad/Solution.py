import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the max pooling operation
max_pooling_op = tf.raw_ops.MaxPoolGrad(
    inputs=input_tensor,
    output_backprop=input_tensor,
    ksize=[2, 2],
    strides=[2, 2],
    padding='VALID'
)

# Compute the gradients
gradients = max_pooling_op.grad

# Print the gradients
print(gradients)
