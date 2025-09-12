import tensorflow as tf

# Define input tensor
input_tensor = tf.constant(value=[[[[1.0, 2.0, 3.0],
                                    [4.0, 5.0, 6.0],
                                    [7.0, 8.0, 9.0]]]], dtype=tf.float32)

# Define filter tensor
filter_tensor = tf.constant(value=[[[[1.0, 2.0, 3.0],
                                     [4.0, 5.0, 6.0],
                                     [7.0, 8.0, 9.0]]]], dtype=tf.float32)

# Compute gradients of convolution with respect to the filter
grads = tf.raw_ops.Conv2DBackpropFilter(input=input_tensor,
                                        filter=filter_tensor,
                                        strides=[1, 1, 1, 1],
                                        padding="VALID")

print(grads)
