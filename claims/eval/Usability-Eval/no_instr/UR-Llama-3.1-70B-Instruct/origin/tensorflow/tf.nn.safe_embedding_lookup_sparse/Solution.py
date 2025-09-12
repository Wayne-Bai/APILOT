import tensorflow as tf

# Define a simple function to lookup embedding results.
# Invalid IDs will result in a vector of zeros, and empty features will return an empty tensor.
def lookup_embedding(embedding_matrix, ids, max_id):
    # Get the embedding size
    embedding_size = embedding_matrix.shape[1]
    
    # Replace invalid IDs with 0
    valid_ids = tf.where(ids < max_id, ids, tf.zeros_like(ids))
    
    # Mask to handle empty features
    mask = tf.cast(ids!= 0, tf.bool)
    
    # Lookup embedding results
    embedding_results = tf.gather(embedding_matrix, valid_ids)
    
    # Mask out invalid IDs and handle empty features
    masked_results = tf.where(tf.tile(mask[..., tf.newaxis], [1, embedding_size]), embedding_results, tf.zeros_like(embedding_results))
    
    return masked_results


# Example usage:
embedding_matrix = tf.random.uniform((100, 10))  # Sample embedding matrix (100 IDs, 10-dimensional embeddings)
ids = tf.constant([[1, 2, 3, 0, 101], [5, 0, 0, 7, 8]])  # Sample IDs, including invalid (101) and empty (0) values
max_id = 100  # Maximum valid ID

results = lookup_embedding(embedding_matrix, ids, max_id)
print(results)
