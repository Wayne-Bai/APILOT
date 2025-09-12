import tensorflow as tf

# Generate sample input data
input_data = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])

# Shuffle the input data
shuffled_data = tf.random.shuffle(input_data)

# Print the shuffled data
print(shuffled_data.numpy())
