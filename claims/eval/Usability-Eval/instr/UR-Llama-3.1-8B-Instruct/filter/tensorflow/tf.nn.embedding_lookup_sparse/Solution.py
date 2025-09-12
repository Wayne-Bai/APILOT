# Import necessary libraries
import tensorflow as tf

# Define a list of tensors with embeddings
# Each tensor can have a different number of dimensions
tensors = [
    tf.constant([[1, 2, 3], [4, 5, 6]]),
    tf.constant([[7, 8, 9], [10, 11, 12], [13, 14, 15]]),
    tf.constant([[16, 17, 18]])
]

# Function to look up embeddings for given ids and weights
def lookup_embeddings(ids, weights, tensors):
    # Check if the id is within the valid range
    ids = tf.check_numerics(ids, 'Invalid id')
    
    # Get the embedding tensor based on the given id
    embeddings = tf.gather(tensors, ids)
    
    # Calculate the weighted sum of embeddings
    weighted_embeddings = tf.einsum('bd,bc->bc', weights, embeddings)
    
    return weighted_embeddings

# Example usage
ids = tf.constant([0, 1])  # Look up embeddings for id 0 and 1
weights = tf.constant([[0.5, 0.5], [0.7, 0.3]])  # Weights for each dimension

result = lookup_embeddings(ids, weights, tensors)
print(result)
