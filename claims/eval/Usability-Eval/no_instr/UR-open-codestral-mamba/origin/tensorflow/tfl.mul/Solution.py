import tensorflow as tf

# Define two tensors of the same shape
tensor1 = tf.constant([1, 2, 3, 4, 5], shape=[5, 1])
tensor2 = tf.constant([5, 4, 3, 2, 1], shape=[5, 1])

# Perform element-wise multiplication
result = tf.multiply(tensor1, tensor2)

# Print the result
print("Element-wise multiplication result is: ", result)
