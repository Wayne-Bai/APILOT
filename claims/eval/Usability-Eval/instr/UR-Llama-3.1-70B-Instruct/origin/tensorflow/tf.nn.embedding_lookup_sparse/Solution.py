import tensorflow as tf

def lookup_embeddings(ids, tensors):
    """
    Looks up embeddings for the given ids and weights from a list of tensors.

    Args:
        ids (tf.Tensor): A tensor of indices to look up in the embedding tensors.
        tensors (list of tf.Tensor): A list of tensors representing the embedding values.

    Returns:
        tf.Tensor: A tensor of shape (ids.shape[0], embedding_dim) representing the looked up embeddings.
    """

    # Check if ids is a tensor
    if not isinstance(ids, tf.Tensor):
        ids = tf.convert_to_tensor(ids, dtype=tf.int32)

    # Check if all elements in tensors are tensors
    if not all(isinstance(tensor, tf.Tensor) for tensor in tensors):
        raise ValueError("All elements in tensors must be tensors")

    # Calculate the total embedding dimension
    embedding_dim = sum(tensor.shape[-1] for tensor in tensors)

    # Initialize the embeddings tensor with zeros
    embeddings = tf.zeros((ids.shape[0], embedding_dim), dtype=tf.float32)

    # Iterate over each tensor in the list
    start_idx = 0
    for tensor in tensors:
        # Calculate the embedding dimension for this tensor
        tensor_embedding_dim = tensor.shape[-1]

        # Use tf.gather to look up the embeddings for the given ids in this tensor
        tensor_embeddings = tf.gather(tensor, ids)

        # Add the looked up embeddings to the total embeddings
        embeddings[:, start_idx:start_idx + tensor_embedding_dim] = tensor_embeddings

        # Increment the start index
        start_idx += tensor_embedding_dim

    return embeddings


# Example usage
ids = tf.constant([0, 1, 2])
tensors = [tf.constant([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]),
           tf.constant([[0.7, 0.8], [0.9, 1.0], [1.1, 1.2]])]

embeddings = lookup_embeddings(ids, tensors)
print(embeddings)
