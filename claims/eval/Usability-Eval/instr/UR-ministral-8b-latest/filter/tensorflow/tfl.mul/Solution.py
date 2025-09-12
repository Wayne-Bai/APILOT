import tensorflow as tf

# Create two random tensors
tensor1 = tf.constant([[1, 2, 3], [4, 5, 6]])
tensor2 = tf.constant([[10, 20, 30], [40, 50, 60]])

# Perform element-wise multiplication
result = tf.multiply(tensor1, tensor2)

# Run the operation and print the result
print(result.numpy())
