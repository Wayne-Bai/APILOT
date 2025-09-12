import tensorflow as tf

# Define two tensors
tensor1 = tf.constant([1, 2, 3])
tensor2 = tf.constant([4, 5, 6])

# Perform element-wise multiplication
result = tf.multiply(tensor1, tensor2)

# Print the result
print(result.numpy())
