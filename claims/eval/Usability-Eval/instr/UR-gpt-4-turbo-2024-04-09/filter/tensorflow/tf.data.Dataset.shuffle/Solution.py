import tensorflow as tf

# Create some example input data
input_data = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])

# Randomly shuffle the data
shuffled_data = tf.random.shuffle(input_data)

# Print the original and shuffled data
print("Original data:")
print(input_data.numpy())

print("Shuffled data:")
print(shuffled_data.numpy())
