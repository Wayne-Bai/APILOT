import tensorflow as tf
# Define the embedding matrix
embedding_matrix = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
# Define the input IDs tensor
input_ids = tf.constant([0, 1, 2, 3])
# Define the empty feature mask tensor
empty_feature_mask = tf.constant([True, False, False, True])
# Define the lookup embedding results with invalid IDs and empty features handling
lookup_results = tf.gather(embedding_matrix, input_ids)
lookup_results = tf.where(empty_feature_mask, tf.zeros_like(lookup_results), lookup_results)
# Print the lookup embedding results
print(lookup_results)
