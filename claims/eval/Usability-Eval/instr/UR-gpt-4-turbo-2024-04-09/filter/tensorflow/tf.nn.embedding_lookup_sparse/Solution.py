import tensorflow as tf

def lookup_embeddings(ids, weight_list):
    # Create a TensorArray to gather the results
    gathered_embeddings = tf.TensorArray(dtype=tf.float32, size=len(weight_list))

    # Loop through the weight_list tensors and gather embeddings by ids
    for i, weights in enumerate(weight_list):
        # Use `tf.gather` to retrieve embeddings by ids
        gathered = tf.gather(weights, ids)
        gathered_embeddings = gathered_embeddings.write(i, gathered)

    # Stack all gathered embeddings into a single tensor
    result_embeddings = gathered_embeddings.stack()

    return result_embeddings

# Example usage:
# Define some weight tensors (simulating embedding matrices)
weight_tensor1 = tf.constant([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
weight_tensor2 = tf.constant([[0.7, 0.8], [0.9, 1.0], [1.1, 1.2]])

# Ids to lookup in the weight tensors
ids = tf.constant([0, 2])

# List of weight tensors
weights = [weight_tensor1, weight_tensor2]

# Call the function
embeddings = lookup_embeddings(ids, weights)
print(embeddings)
