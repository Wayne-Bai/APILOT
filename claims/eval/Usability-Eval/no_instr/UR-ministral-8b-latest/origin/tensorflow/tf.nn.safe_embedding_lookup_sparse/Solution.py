import tensorflow as tf
import numpy as np

# Dummy data
ids = [1, 2, 3, 4, 5]
invalid_id = -1
empty_features = 0

# Dummy lookup table
lookup_table = {
    1: tf.constant([0.1, 0.2, 0.3]),
    2: tf.constant([0.4, 0.5, 0.6]),
    3: tf.constant([0.7, 0.8, 0.9]),
    4: tf.constant([0.0, 0.0, 0.0]),
    5: tf.constant([0.1, 0.1, 0.1]),
}

def get_embedding(id, lookup_table):
    if id in lookup_table:
        return lookup_table[id]
    else:
        return tf.constant([0.0, 0.0, 0.0])  # Default to zeros for invalid ID

embeddings = []

for id in ids:
    embedding = get_embedding(id, lookup_table)
    embeddings.append(embedding.numpy())

# Handle empty features
for i, feature in enumerate(embeddings):
    if np.all(np.equal(feature, [0.0, 0.0, 0.0])):
        embeddings[i] = np.array([0.5, 0.5, 0.5])  # Replace with a value for empty features

print("Embeddings:", embeddings)

# Invalid ID example
invalid_embedding = get_embedding(invalid_id, lookup_table)
print("Invalid ID Embedding:", invalid_embedding.numpy())

# Handle invalid ID example
if not tf.reduce_all(tf.equal(invalid_embedding, tf.constant([0.0, 0.0, 0.0]))):
    print("Invalid ID is handled properly!")
else:
    print("Invalid ID still has errors.")
