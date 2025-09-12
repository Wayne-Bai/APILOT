import tensorflow as tf

# Assuming you have a tensor `data` with shape (batch_size, num_features)
# Replace `data` with your actual tensor
data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Randomly shuffle the data
shuffled_data = tf.random.shuffle(data)

print(shuffled_data)
