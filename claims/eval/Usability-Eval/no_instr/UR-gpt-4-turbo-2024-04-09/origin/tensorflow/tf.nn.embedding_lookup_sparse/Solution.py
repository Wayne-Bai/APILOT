import tensorflow as tf

def lookup_embeddings(ids, weights, embedding_tensors_list):
    concatenated_embeddings = tf.concat(embedding_tensors_list, axis=0)
    selected_embeddings = tf.nn.embedding_lookup(concatenated_embeddings, ids)
    weighted_embeddings = selected_embeddings * tf.expand_dims(weights, axis=-1)
    return weighted_embeddings

# Example usage
# Suppose we have two embedding tensors for categories and items respectively
categories_embeddings = tf.random.normal([10, 64])  # 10 categories, 64-dimensional embeddings
items_embeddings = tf.random.normal([20, 64])       # 20 items, 64-dimensional embeddings

# Example IDs and their respective weights
ids = tf.constant([0, 15, 5, 10])
weights = tf.constant([0.5, 0.3, 1.0, 0.7])

# Call function
resulting_embeddings = lookup_embeddings(ids, weights, [categories_embeddings, items_embeddings])
print(resulting_embeddings)
