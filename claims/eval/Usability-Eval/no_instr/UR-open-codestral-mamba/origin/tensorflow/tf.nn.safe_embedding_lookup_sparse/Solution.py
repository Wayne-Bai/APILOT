import tensorflow as tf
from tensorflow.keras.layers import Embedding

def lookup_embedding(embedding_layer, inputs):
    embedded_inputs = embedding_layer(inputs)
    # Check for invalid IDs
    is_valid_id = tf.reduce_any(tf.not_equal(inputs, 0), axis=1)
    # Check for empty features
    is_empty_feature = tf.not_equal(tf.reduce_sum(embedded_inputs, axis=2), 0)
    # Set embeddings of invalid IDs and empty features to zeros
    valid_embedded_inputs = tf.where(is_valid_id & is_empty_feature, embedded_inputs, tf.zeros_like(embedded_inputs))
    return valid_embedded_inputs

# Create an embedding layer
vocab_size = 10000
embedding_dim = 128
embedding_layer = Embedding(vocab_size, embedding_dim)

# Assume input ids
input_ids = tf.constant([[1, 2, 3], [4, 5, 0], [6, 7, 8], [9, 10, 0], [0, 0, 0]])

lookup_results = lookup_embedding(embedding_layer, input_ids)
print(lookup_results)
