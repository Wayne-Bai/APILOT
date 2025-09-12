import tensorflow as tf

# Assuming the following inputs
ids = [[1, 2, 3], [4, 5, 6]]  # List of ids to look up embeddings for
weights = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]  # List of weights for each id
tensors = [tf.constant([0.1, 0.2, 0.3], dtype=tf.float32), tf.constant([0.4, 0.5, 0.6], dtype=tf.float32)]  # List of tensors to look up embeddings from

# Create a new tensor by looked up embeddings for the given ids and weights from a list of tensors
output = tf.gather_nd(tensors, ids, axis=0, batch_dims=1)
output_weighted = tf.reduce_sum(output * weights, axis=1)

# Print the result
print(output_weighted)
