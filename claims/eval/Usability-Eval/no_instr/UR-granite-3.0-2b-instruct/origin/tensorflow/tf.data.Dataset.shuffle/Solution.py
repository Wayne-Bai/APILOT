import tensorflow as tf

# Assume that x is your input data
# x = tf.constant([1, 2, 3, 4, 5])

# Shuffle the input data
shuffled_data = tf.shuffle(x)

# Print the shuffled data
print(shuffled_data)
