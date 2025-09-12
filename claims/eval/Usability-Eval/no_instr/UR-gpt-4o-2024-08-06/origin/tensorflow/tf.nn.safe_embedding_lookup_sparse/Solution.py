import tensorflow as tf

# Create a list of vocabulary words
vocabulary_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Create a lookup table for vocabulary
initializer = tf.lookup.KeyValueTensorInitializer(
    keys=vocabulary_list,
    values=tf.range(len(vocabulary_list), dtype=tf.int64),
    key_dtype=tf.string,
    value_dtype=tf.int64
)
lookup_table = tf.lookup.StaticHashTable(
    initializer=initializer, 
    default_value=-1
)

# Create an embedding layer
embedding_dim = 3
embedding_matrix = tf.Variable(
    tf.random.uniform([len(vocabulary_list), embedding_dim], -1.0, 1.0), 
    trainable=True
)

# Function to get embeddings for given words
def get_embedding(words):
    # Lookup IDs from the table
    ids = lookup_table.lookup(words)
    # Lookup embeddings, handle default value (e.g., for unknown words or empty inputs)
    valid_ids = tf.maximum(ids, 0)
    # Lookup embeddings
    embeddings = tf.nn.embedding_lookup(embedding_matrix, valid_ids)
    # Return -1 embeddings for invalid IDs (way to handle invalid)
    mask = tf.greater_equal(ids, 0)
    return tf.where(tf.expand_dims(mask, -1), embeddings, tf.fill(tf.shape(embeddings), -1.0))

# Example input
words_to_lookup = tf.constant(['banana', 'cherry', 'fig', 'apple', 'grape'])

# Get embeddings
embedding_results = get_embedding(words_to_lookup)

# Print embeddings
print(embedding_results)
