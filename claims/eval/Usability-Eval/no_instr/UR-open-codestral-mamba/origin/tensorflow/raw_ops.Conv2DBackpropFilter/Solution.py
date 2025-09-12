import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[[[1., 2., 3.],
                              [4., 5., 6.]],

                             [[7., 8., 9.],
                              [10., 11., 12.]]]], dtype=tf.float32)

# Define the filter tensor
filter_tensor = tf.constant([[[[1., 0.],
                               [0., 1.]]],

                              [[[1., 0.],
                                [0., 1.]]]], dtype=tf.float32)

# Compute the convolution
conv = tf.raw_ops.Conv2D(input=input_tensor, filters=filter_tensor, strides=[1, 1, 1, 1], padding="VALID")

# Compute the gradients
grads = tf.raw_ops.Conv2DBackpropInput(input=conv, filters=filter_tensor, out_backprop=tf.ones_like(conv), strides=[1, 1, 1, 1], padding="VALID")

# Print the gradients
print(grads)
