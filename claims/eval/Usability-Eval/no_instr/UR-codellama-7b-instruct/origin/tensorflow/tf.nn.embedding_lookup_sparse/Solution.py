
import tensorflow as tf

# Define the list of tensors
tensors = [tf.constant([[1, 2], [3, 4]]), tf.constant([[5, 6], [7, 8]])]

# Define the ids and weights for each tensor
ids = [0, 1, 2]
weights = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]

# Use tf.gather to lookup the embeddings for the given ids and weights
result = tf.gather(tensors, ids)
