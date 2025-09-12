import tensorflow as tf

# Define input and filter tensors
input_tensor = tf.random.normal(shape=(1, 28, 28, 1))  # Example input: batch of 1, 28x28 image with 1 channel
filter_tensor = tf.random.normal(shape=(3, 3, 1, 16))   # Example filter: 3x3 size, 1 input channel, 16 output channels

# Perform 2-D convolution
output_tensor = tf.nn.conv2d(input=input_tensor,
                              filters=filter_tensor,
                              strides=[1, 1, 1, 1],
                              padding='VALID')

# Print the output shape
print(output_tensor.shape)
