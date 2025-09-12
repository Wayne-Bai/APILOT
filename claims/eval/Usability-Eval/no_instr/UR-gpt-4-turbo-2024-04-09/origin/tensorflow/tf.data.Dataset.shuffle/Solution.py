import tensorflow as tf

# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_tensor = tf.constant(data)

# Shuffle the data
shuffled_data = tf.random.shuffle(data_tensor)

print("Original data:", data)
print("Shuffled data:", shuffled_data.numpy())
