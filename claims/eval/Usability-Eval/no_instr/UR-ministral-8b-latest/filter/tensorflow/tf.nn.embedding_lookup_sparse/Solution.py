import tensorflow as tf

# Example IDs and a list of weights
ids = tf.constant([[1, 2, 3], [4, 5, 6]])  # Example IDs
weights = tf.constant([[0.1, 0.2, 0.3],
                       [0.4, 0.5, 0.6]])  # Example weights

embeddings = tf.constant([[10.0, 20.0, 30.0],
                          [40.0, 50.0, 60.0],
                          [70.0, 80.0, 90.0]])  # Example embeddings for IDs 1 to 3

# Look up embeddings for given IDs and apply corresponding weights
embedding_lookup = tf.gather(embeddings, ids, axis=0, batch_dims=1)
weight_application = tf.expand_dims(weights, axis=-1)
multiply = embedding_lookup * weight_application
result = tf.reduce_sum(multiply, axis=1)

print(result)
