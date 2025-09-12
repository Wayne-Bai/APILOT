import tensorflow as tf

# Define input parameters
input_data = tf.constant([[[[1.0], [2.0]], [[3.0], [4.0]]]], dtype=tf.float32)
filter_shape = [2, 2, 1, 1]  # [filter_height, filter_width, in_channels, out_channels]
out_backprop = tf.constant([[[[1.0], [2.0]], [[3.0], [4.0]]]], dtype=tf.float32)
strides = [1, 1, 1, 1]
padding = 'VALID'

# Ensure the filter is initialized correctly
filter = tf.Variable(tf.random.normal(filter_shape), trainable=True)

# Create convolutional layer
conv_layer = tf.nn.conv2d(input_data, filter, strides=strides, padding=padding)

# Define a simple loss function which is square of the convolution result
loss = tf.reduce_sum(tf.square(conv_layer - out_backprop))

# Compute gradients with respect to the filter
with tf.GradientTape() as tape:
    conv_layer = tf.nn.conv2d(input_data, filter, strides=strides, padding=padding)
    loss = tf.reduce_sum(tf.square(conv_layer - out_backprop))

grads = tape.gradient(loss, filter)

print("Gradients with respect to the filter:")
print(grads)
