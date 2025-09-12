import tensorflow as tf

# Assuming we have a list of embeddings tensors and their corresponding ids
embeddings = [tf.random.normal((100, 20)) for _ in range(5)]
ids = [tf.random.uniform([100, 1], maxval=5, dtype=tf.int32) for _ in range(3)]

# Create a dictionary to map ids to their corresponding tensors
embedding_dict = {id_item[0]: embedding for id_item, embedding in zip(tf.concat(ids, 0), tf.concat(embeddings, 0))}

# Look up the embeddings based on the given ids
def lookup_embeddings(ids, embedding_dict):
    lookup_ids = tf.nn.embedding_lookup(ids, embedding_dict)
    return lookup_ids

# Example usage
lookup_ids = lookup_embeddings(tf.constant([23, 34, 12]), embedding_dict)
print(lookup_ids)
