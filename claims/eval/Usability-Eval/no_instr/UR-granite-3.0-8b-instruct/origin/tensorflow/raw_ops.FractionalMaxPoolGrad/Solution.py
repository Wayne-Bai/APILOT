import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0],
                             [5.0, 6.0, 7.0, 8.0],
                             [9.0, 10.0, 11.0, 12.0]], tf.float32)

# Define the output tensor
output_tensor = tf.constant([[1.0, 2.0],
                              [5.0, 6.0],
                              [9.0, 10.0]], tf.float32)

# Compute the gradient of the FractionalMaxPool function
gradient = tf.raw_ops.FractionalMaxPoolGrad(input=input_tensor, output=output_tensor, pool_size=2, padding='SAME')

print(gradient)
