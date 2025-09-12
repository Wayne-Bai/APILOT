import tensorflow as tf

def find_k_largest_entries(input_tensor, k):
    # Get the shape of the input tensor
    shape = tf.shape(input_tensor)

    # Flatten the input tensor
    flat_tensor = tf.reshape(input_tensor, [-1])

    # Find the k largest entries and their indices
    k_largest, k_indices = tf.nn.top_k(flat_tensor, k)

    # Reshape the indices to match the original tensor shape
    k_indices = tf.reshape(k_indices, shape[:-1])

    return k_largest, k_indices
