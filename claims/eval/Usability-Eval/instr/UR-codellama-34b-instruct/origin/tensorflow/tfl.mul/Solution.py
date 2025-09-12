
import tensorflow as tf

# Define two tensors for input
x = tf.constant([1, 2, 3])
y = tf.constant([4, 5, 6])

# Perform element-wise multiplication
result = x * y

print(result) # [4, 10, 18]
