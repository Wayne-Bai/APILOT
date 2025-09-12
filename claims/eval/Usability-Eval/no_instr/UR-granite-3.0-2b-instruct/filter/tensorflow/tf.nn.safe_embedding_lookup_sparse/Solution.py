import tensorflow as tf

# Assuming that you have a list of IDs and a dictionary of embeddings
ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
embeddings = {
    1: [0.1, 0.2, 0.3],
    2: [0.4, 0.5, 0.6],
    3: [0.7, 0.8, 0.9],
    4: [1.0, 1.1, 1.2],
    5: [1.3, 1.4, 1.5],
    6: [1.6, 1.7, 1.8],
    7: [1.9, 2.0, 2.1],
    8: [2.2, 2.3, 2.4],
    9: [2.5, 2.6, 2.7],
    10: [2.8, 2.9, 3.0]
}

# Create a TensorFlow tensor for the embeddings
embeddings_tensor = tf.constant(embeddings)

# Create a TensorFlow tensor for the IDs
ids_tensor = tf.constant(ids)

# Create a TensorFlow function to look up the embeddings
def lookup_embeddings(ids):
    # Get the embeddings for the given IDs
    embeddings = tf.gather(embeddings_tensor, ids_tensor)

    # Check for invalid IDs and return None if an ID is not found
    invalid_ids = tf.where(tf.logical_not(tf.in_range(ids_tensor, 0, len(embeddings))))
    embeddings = tf.gather(embeddings, invalid_ids)

    return embeddings

# Test the function
print(lookup_embeddings(ids))
