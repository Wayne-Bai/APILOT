import tensorflow as tf

# Define the weights and biases for the convolution layer
filters = tf.Variable(tf.random_normal([5, 5, 3, 64], mean=0.0, stddev=1.0))
bias = tf.Variable(tf.zeros([64]))

# Define the input and output shapes for the convolution layer
input_shape = (224, 224, 3)
output_shape = (224, 224, 64)

# Create a placeholder for the input data
x = tf.placeholder(tf.float32, shape=input_shape)

# Create a convolutional layer
y = tf.nn.conv2d(x, filters, strides=[1, 1, 1, 1], padding='SAME')

# Add the bias to the output of the convolution layer
y = y + bias

# Compute the gradients of the convolution with respect to the input
dx = tf.gradients(y, x)

# Print the gradient values
print("Gradient values:", dx[0].numpy())
