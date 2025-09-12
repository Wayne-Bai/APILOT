import tensorflow as tf

# Define the inputs
ids = [1, 2, 3, 4, 5]
weights = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]

# Define the embedding table
embedding_table = tf.keras.layers.Embedding(input_dim=3, output_dim=3)

# Look up the embeddings for the given IDs and weights
lookups = [embedding_table(id) * weight for id, weight in zip(ids, weights)]

# Combine the lookups into a single tensor
output = tf.concat(lookups, axis=0)

print(output)
