import tensorflow as tf

# Assuming USER_EMBEDDING_IDS and USER_EMBEDDING_WEIGHTS are defined tensors

embedding_ids = tf.constant(USER_EMBEDDING_IDS, dtype=tf.int32)
embedding_weights = tf.constant(USER_EMBEDDING_WEIGHTS, dtype=tf.float32)

# Assuming EMBEDDING_MATRIX is a pre-trained embedding matrix

embedding_matrix = tf.Variable(EMBEDDING_MATRIX, trainable=False, dtype=tf.float32)

# Lookup embeddings for the given ids and weights
embeddings = tf.nn.embedding_lookup(embedding_matrix, embedding_ids, partition_strategy="div")
embeddings_weighted = tf.multiply(embeddings, embedding_weights)
