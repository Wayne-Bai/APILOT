import tensorflow as tf

# Example data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Convert data to TensorFlow tensor
data_tensor = tf.constant(data)

# Shuffle the data
shuffled_data = tf.data.Dataset.from_tensors(data_tensor)
shuffled_data = shuffled_data.shuffle(buffer_size=len(data))

# Convert the TensorFlow dataset to a list to view the shuffled data
shuffled_data_list = list(shuffled_data)

shuffled_data_list
