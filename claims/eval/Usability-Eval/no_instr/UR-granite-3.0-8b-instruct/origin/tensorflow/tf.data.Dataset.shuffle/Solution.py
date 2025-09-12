import tensorflow as tf

# Assuming you have a tensor 'data' with shape (batch_size, num_features)
# and you want to shuffle it.

# First, let's create a tensor with the same shape as 'data'
# but filled with random indices.
random_indices = tf.random.shuffle(tf.range(tf.shape(data)[0]))

# Now, we can use these random indices to shuffle the 'data' tensor.
shuffled_data = tf.gather(data, random_indices)
