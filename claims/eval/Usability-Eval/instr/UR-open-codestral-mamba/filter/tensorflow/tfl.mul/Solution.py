import tensorflow as tf

# Define two tensors
tensor1 = tf.constant([1, 2, 3, 4, 5])
tensor2 = tf.constant([5, 4, 3, 2, 1])

# Element-wise multiplication
result = tf.multiply(tensor1, tensor2)

print(result)
