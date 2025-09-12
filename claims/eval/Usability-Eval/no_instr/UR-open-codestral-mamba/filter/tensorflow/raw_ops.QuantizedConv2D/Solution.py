import tensorflow as tf

# Define the input and filter tensors
input_tensor = tf.constant([[[[1.0, 2.0], [3.0, 4.0]]]], dtype=tf.float32)
filter_tensor = tf.constant([[[[0.1, 0.2], [0.3, 0.4]]]], dtype=tf.float32)

# Perform the 2D convolution operation
result = tf.raw_ops.QuantFused2DConvolution(
    input=input_tensor,
    filter=filter_tensor,
    bias=tf.convert_to_tensor([0.1]),
    strides=[1, 1, 1, 1],
    padding='VALID',
    dilations=[1, 1, 1, 1]
)

print(result)
