import tensorflow as tf

# Create a placeholder for the input tensor
input_tensor = tf.placeholder(tf.float32, shape=[None, None, None, None])

# Create a placeholder for the pooling indices
pooling_indices = tf.placeholder(tf.int32, shape=[None, None, None, None])

# Compute the gradient of the FractionalAvgPool function
grad = tf.raw_ops.FractionalAvgPoolGrad(
    orig_input_shape=input_tensor.shape,
    orig_output_shape=pooling_indices.shape,
    out_backprop=tf.ones_like(pooling_indices),
    pooling_indices=pooling_indices
)

# Print the gradient
print(grad)
