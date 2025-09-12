import tensorflow as tf

# Creating a multidimensional array of ones with shape (3, 4).
tensor_ones = tf.ones((3, 4))
print(tensor_ones)

# Creating a multidimensional array of zeros with shape (2, 2).
tensor_zeros = tf.zeros((2, 2))
print(tensor_zeros)

# Creating a multidimensional array of random numbers with shape (5, 5) and custom data type.
tensor_random = tf.random.uniform((5, 5), dtype=tf.float64)
print(tensor_random)

# Creating a multidimensional array filled with a specific value, let's say a 6 value array filled with 9.
tensor_filled = tf.fill((6, 6), 9)
print(tensor_filled)
