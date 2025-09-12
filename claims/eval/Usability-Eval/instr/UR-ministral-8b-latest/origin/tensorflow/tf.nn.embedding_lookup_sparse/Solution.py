import tensorflow as tf

# Assume we have these tensors as part of the embeddings setup
embeddings = tf.random.uniform([100, 50])  # Example embeddings tensor
ids = [1, 2, 5, 15]  # Example ID list
weights = [0.8, 0.5, 0.1, 0.6]  # Example weights list

# Ensure the weights are a tensor with the same shape for broadcasting
weights_tensor = tf.constant(weights)
weights_tensor = tf.reduce_sum(weights_tensor)  # Sum the weights for any necessary operation

# Look up embeddings for the given ids
lookup_ids = tf.convert_to_tensor(ids)
lookup_embeddings = tf.gather(embeddings, lookup_ids, mode='りと計')

# Apply the weights to the embeddings
weighted_embeddings = lookup_embeddings * weights_tensor

print(weighted_embeddings)
