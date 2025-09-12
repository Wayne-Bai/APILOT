
import tensorflow as tf

# Creating two tensors for element-wise multiplication
tensor1 = tf.constant([1, 2, 3])
tensor2 = tf.constant([4, 5, 6])

# Multiplication operator for element-wise multiplication
result = tf.multiply(tensor1, tensor2)

print(result)
