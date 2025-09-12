import tensorflow as tf

# Define two tensors
tensor1 = tf.constant([1, 2, 3, 4, 5])
tensor2 = tf.constant([6, 7, 8, 9, 10])

# Perform element-wise multiplication
result = tf.multiply(tensor1, tensor2)

# Print the result
print(result)
