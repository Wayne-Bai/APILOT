import tensorflow as tf

# Create a constant tensor from a tensor-like object
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])

result = tf.add(a, b)

# Print the result
print(result)
