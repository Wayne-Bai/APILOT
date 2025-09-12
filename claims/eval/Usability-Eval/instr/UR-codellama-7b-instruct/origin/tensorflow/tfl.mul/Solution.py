import tensorflow as tf

# Element-wise multiplication
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
c = tf.multiply(a, b)
print(c)
