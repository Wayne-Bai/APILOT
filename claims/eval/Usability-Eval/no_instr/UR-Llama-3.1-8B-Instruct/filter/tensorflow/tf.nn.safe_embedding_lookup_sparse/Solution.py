import tensorflow as tf

class EmbeddingLookup():
    def __init__(self, vocabulary_size, embedding_dim, word2id):
        """
        Args:
            vocabulary_size (int): The size of the vocabulary.
            embedding_dim (int): The dimension of the embedding.
            word2id (dict): A dictionary that maps words to their IDs.
        """
        self.vocabulary_size = vocabulary_size
        self.embedding_dim = embedding_dim
        self.word2id = word2id
        self.embedding_matrix = tf.Variable(tf.random.uniform([vocabulary_size, embedding_dim]), trainable=True)

    def lookup(self, ids):
        """
        Looks up the embedding for the given IDs.

        Args:
            ids (Tensor): A tensor of IDs.

        Returns:
            A tensor of shape [batch_size, embedding_dim].
        """
        # Use tf.gather to look up the embedding matrix
        embedding = tf.gather(self.embedding_matrix, ids)

        # If invalid IDs are present, set the corresponding embedding to zero
        if self.vocabulary_size > 0:
            zeros = tf.zeros((tf.shape(ids)[0], self.embedding_dim))
            mask = tf.cast(tf.math.is_in_range(ids, 0, self.vocabulary_size), tf.int32)
            embedding = tf.where(mask, embedding, zeros)

        # If the input features are empty, return a tensor of zeros
        if tf.size(ids) == 0:
            return tf.zeros((0, self.embedding_dim))

        # Return the embedding
        return embedding

# Example usage:
word2id = {"word1": 0, "word2": 1, "word3": 2}
vocabulary_size = len(word2id)
embedding_dim = 5
lookup = EmbeddingLookup(vocabulary_size, embedding_dim, word2id)
ids = tf.constant([0, 1, 2, 3])  # including an invalid ID
print(lookup.lookup(ids))
