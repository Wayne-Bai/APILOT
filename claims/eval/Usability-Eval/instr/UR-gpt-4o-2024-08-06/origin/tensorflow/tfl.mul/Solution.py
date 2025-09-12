import tensorflow as tf

# Creating two example tensors for element-wise multiplication
tensor1 = tf.constant([2, 4, 6], dtype=tf.float32)
tensor2 = tf.constant([3, 5, 7], dtype=tf.float32)

# Performing element-wise multiplication
result = tf.multiply(tensor1, tensor2)

print("Result of element-wise multiplication:", result.numpy())
