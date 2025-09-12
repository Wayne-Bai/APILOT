import tensorflow as tf

# Create tensors
A = tf.constant([1.0, 2.0, 3.0])
B = tf.constant([4.0, 5.0, 6.0])

# Perform element-wise multiplication
C = A * B

# Print the result
print(C.numpy())
