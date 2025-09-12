import tensorflow as tf

# Create a random tensor with shape (2, 3)
input_tensor = tf.random.normal((2, 3))

# Create a tensor of all ones with the same shape as the input
ones_tensor = tf.ones(input_tensor.shape, dtype=tf.float32)

print("Input tensor:", input_tensor)
print("Ones tensor:", ones_tensor)
