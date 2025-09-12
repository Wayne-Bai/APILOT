import tensorflow as tf

# Element-wise multiplication operation
def elementwise_multiplication(tensor_a, tensor_b):
    return tf.multiply(tensor_a, tensor_b)

# Sample tensors
tensor_a = tf.constant([1, 2, 3])
tensor_b = tf.constant([4, 5, 6])

# Perform element-wise multiplication
result = elementwise_multiplication(tensor_a, tensor_b)
print(result)
