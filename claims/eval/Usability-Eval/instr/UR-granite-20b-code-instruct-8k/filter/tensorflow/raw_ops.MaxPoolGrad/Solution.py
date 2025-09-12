import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Define the maxpooling operation
pool = tf.nn.max_pool(input_tensor, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Define the gradients of the maxpooling operation
pool_grad = tf.raw_ops.MaxPoolGrad(orig_input=input_tensor, orig_output=pool, grad=tf.ones_like(pool))

# Print the gradients
print(pool_grad)
