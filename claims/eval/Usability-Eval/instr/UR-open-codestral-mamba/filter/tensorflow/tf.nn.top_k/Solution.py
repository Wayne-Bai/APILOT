import tensorflow as tf

# Define tensor
x = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define k (number of largest entries to find)
k = 2

# Use tf.math.top_k()
top_k = tf.math.top_k(x, k=k)

# The top_k result is a SparseTensor object containing the k largest elements along each row
print(top_k)
