import tensorflow as tf

# Define the lookup table
vocab_size = 1000  # Change this according to your vocabulary
embedding_dim = 50  # Change this according to your need
initializer = tf.random_uniform_initializer(minval=-1.0, maxval=1.0)
table = tf.lookup.StaticHashTable(
    initializer(tf.int64, tf.float32, vocab_size, embedding_dim),
    default_value=tf.zeros([embedding_dim])
)

# List of IDs, may contain invalid IDs and should handle empty lists as well
ids = [1, 2, 1005, 3, 10000, 4]  # Change this according to your data

# Lookup embeddings
embeddings = table.lookup(ids)

# Create a session and run the lookup operation
with tf.Session() as sess:
    sess.run(tf.tables_initializer())
    result = sess.run(embeddings)
    print(result)
