import tensorflow as tf

class EmbeddingLookup:
    def __init__(self, vocab_size, embedding_size, ids):
        self.vocab_size = vocab_size
        self.embedding_size = embedding_size
        self.ids = ids

    def create_embedding_layer(self):
        # Create an embedding layer with the specified vocab size and embedding size
        embedding_layer = tf.keras.layers.Embedding(
            input_dim=self.vocab_size,
            output_dim=self.embedding_size,
            input_length=self.vocab_size,
            embeddings_initializer='uniform',
            trainable=False
        )
        
        # Create a lookup layer that uses the embedding layer to find the embedding for each ID
        lookup = tf.keras.layers.Lambda(
            lambda x: tf.gather(embedding_layer.embedding_weights, x, axis=0, batch_dims=None),
            input_shape=(1,)
        )
        
        return lookup

    def lookup_embedding_results(self, ids):
        # Convert the IDs to a float32 type
        ids = tf.cast(ids, tf.float32)
        
        # Use the lookup layer to find the embedding for each ID
        embedding_results = self.lookup_layer(ids)
        
        # Reshape the embedding results to the correct shape
        embedding_results = tf.tile(embedding_results[:, None, :], [1, ids.shape[1], 1])
        
        # Convert the embedding results to int32 type
        embedding_results = tf.cast(embedding_results, tf.int32)
        
        return embedding_results

    def create_model(self, ids):
        # Create the lookup layer
        self.lookup_layer = self.create_embedding_layer()
        
        # Use the lookup layer to find the embedding for each ID
        embedding_results = self.lookup(data=ids)
        
        return embedding_results


# Example usage:
vocab_size = 1000
embedding_size = 128
ids = tf.random.uniform(shape=(4, 5), minval=0, maxval=vocab_size, dtype=tf.int32)

# Initialize the embedding lookup class
embedding_lookup = EmbeddingLookup(vocab_size, embedding_size, ids)

# Create the model
model = embedding_lookup.create_model(ids=ids)

# Print the embedding results
print(model)
