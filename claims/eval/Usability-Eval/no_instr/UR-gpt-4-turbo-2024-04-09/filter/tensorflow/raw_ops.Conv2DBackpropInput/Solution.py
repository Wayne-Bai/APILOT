import tensorflow as tf

# Define input variables and convolutional filter
input_tensor = tf.Variable(tf.random.normal([1, 10, 10, 3]))  # Example input: batch size = 1, height = 10, width = 10, channels = 3
filter_tensor = tf.Variable(tf.random.normal([3, 3, 3, 8]))  # Example filter: height = 3, width = 3, in_channels = 3, out_channels = 8

# Perform convolution
output = tf.nn.conv2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding="SAME")

# Dummy loss just for gradient computation example (sum of all outputs)
loss = tf.reduce_sum(output)

# Compute gradient of the input w.r.t. the loss
grad_input = tf.gradients(loss, input_tensor)[0]

print("Gradient of the Loss with respect to the Input:")
print(grad_input)
