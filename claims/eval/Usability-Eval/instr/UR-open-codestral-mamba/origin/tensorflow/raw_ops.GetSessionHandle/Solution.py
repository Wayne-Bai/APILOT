import tensorflow as tf

# Create a constant tensor
x = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)

# Capture the tensor value in a session and return a handle to that value
sess = tf.compat.v1.Session()
tensor_handle = sess.handle(x)

# Print the tensor handle
print(tensor_handle)
