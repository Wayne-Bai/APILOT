import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0], shape=[2, 2, 1, 1])

# Define the maxpool2d function
maxpool_2d = tf.nn.max_pool(input_tensor,
                            ksize=[1, 2, 2, 1],
                            strides=[1, 2, 2, 1],
                            padding='SAME')

# Compute the gradient of the maxpooling function
gradients = tf.gradients(maxpool_2d, input_tensor)

# Print the gradients
print(gradients)
