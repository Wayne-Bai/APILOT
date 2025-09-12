import tensorflow as tf

# Assuming you have input tensor 'data' and prediction tensor 'pred'
data = tf.constant([[1, 2, 3], [4, 5, 6]])
pred = tf.constant([[0, 1, 0], [1, 0, 1]])

# Create a tensor with the same shape as 'data' and 'pred'
output = tf.where(pred, data, tf.zeros_like(data))

# Print the output tensor
print(output)
