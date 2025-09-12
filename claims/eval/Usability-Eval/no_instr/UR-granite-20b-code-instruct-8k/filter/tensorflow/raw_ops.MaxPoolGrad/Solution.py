import tensorflow as tf

# Define the input tensor
input = tf.Variable([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])

# Define the maxpooling operation
maxpool = tf.nn.max_pool(input, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Calculate the gradients of the maxpooling operation
grad = tf.raw_ops.MaxPoolGrad(orig_input=input, orig_output=maxpool, grad=tf.ones_like(maxpool), ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Print the result
print(grad)
