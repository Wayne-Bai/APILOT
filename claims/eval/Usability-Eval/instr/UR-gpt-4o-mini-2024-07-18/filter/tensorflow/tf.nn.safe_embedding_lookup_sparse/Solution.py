import tensorflow as tf

# Function to create an embedding layer with valid ID handling
class LookupEmbedding:
    def __init__(self, vocab_size, embedding_dim):
        self.embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)
        
    def lookup(self, input_ids):
        # Replace invalid IDs with a defined default (e.g., 0), which corresponds to padding
        input_ids = tf.where(tf.logical_or(input_ids < 0, input_ids >= self.embedding.input_dim), 
                             tf.zeros_like(input_ids), 
                             input_ids)
        
        # Compute the embeddings using the valid input IDs
        embeddings = self.embedding(input_ids)
        
        # Handle empty features by returning a tensor of zeros of the appropriate shape
        if tf.reduce_sum(tf.cast(tf.equal(input_ids, 0), tf.int32)) == tf.shape(input_ids)[0]:
            return tf.zeros((tf.shape(input_ids)[0], self.embedding.output_dim))
        
        return embeddings

# Example usage
vocab_size = 1000  # Define your vocabulary size
embedding_dim = 64 # Define your embedding dimension

lookup_embedding = LookupEmbedding(vocab_size, embedding_dim)

# Sample input
input_ids = tf.constant([1, 2, -1, 3, 1001])  # Sample input with valid and invalid IDs
embeddings = lookup_embedding.lookup(input_ids)

print(embeddings)
