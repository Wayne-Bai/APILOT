import tensorflow as tf

# Initialize two sample tensors
tensor_a = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)
tensor_b = tf.constant([[7, 8, 9], [10, 11, 12]], dtype=tf.float32)

# Perform element-wise multiplication
element_wise_multiplication = tf.multiply(tensor_a, tensor_b)

# Run a session to compute the result (if using TensorFlow 1.x)
# With TensorFlow 2.x, eager execution is enabled by default
print("Element-wise multiplication result:")
print(element_wise_multiplication.numpy())
