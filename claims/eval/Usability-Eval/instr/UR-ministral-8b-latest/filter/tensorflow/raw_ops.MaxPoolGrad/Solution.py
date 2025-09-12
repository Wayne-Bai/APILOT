import tensorflow as tf

# Example input
input_tensor = tf.Constant(1)
maxpool_op = tf.nn.max_pool2d(input_tensor, ksize=[1, 2, 1, 1], strides=[1, 2, 1, 1], padding='VALID')
output_tensor = maxpool_op[0]

with tf.GradientTape() as tape:
    tape.watch(input_tensor)
    maxpool_result = tf.raw_ops.MaxPool([input_tensor], ksize=[1, 2, 1, 1], strides=[1, 2, 1, 1], padding='VALID')

# Compute the gradients
gradients = tape.gradient(maxpool_result, input_tensor)

print(gradients)
