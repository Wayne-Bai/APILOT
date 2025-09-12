import tensorflow as tf

# Example input data
data = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Randomly shuffle the data
shuffled_data = tf.data.Dataset.from_tensor_slices(data)
shuffled_data = shuffled_data.shuffle(buffer_size=10)

for element in shuffled_data:
    print(element)
