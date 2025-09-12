import tensorflow as tf

# Define the input tensors
input_tensor = tf.constant([[1., 2., 3.], [4., 5., 6.]])
output_tensor = tf.constant([[1., 2., 3.], [4., 5., 6.]])

# Define the max pooling operation
max_pool_op = tf.nn.max_pool(input_tensor, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

# Define the gradient computation
with tf.GradientTape() as tape:
    tape.watch(output_tensor)
    output_grad = tape.gradient(max_pool_op, output_tensor)
