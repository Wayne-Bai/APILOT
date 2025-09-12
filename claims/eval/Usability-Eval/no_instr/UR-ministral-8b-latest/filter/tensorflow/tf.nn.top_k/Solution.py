import tensorflow as tf

def find_k_largest_entries(tensor, k):
    # Convert the tensor to a tensor with a single element from the last dimension
    last_dim = tf.reduce_max(tensor, axis=-1)
    this_element_tensor = tf.squeeze(tensor, axis=-1, name="SqueezedLast")

    # Perform an argmax operation to get the indices of the k largest elements
    sorted_indices = tf.argsort(this_element_tensor, direction="DESCENDING")

    # Gather the indices and values
    values_and_indices = tf.gather(this_element_tensor, sorted_indices, batch_dims=0)
    indices = tf.gather(sorted_indices, tf.range(k), batch_dims=0)

    return values_and_indices, indices

# Example usage
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)
k = 2

values, indices = find_k_largest_entries(tensor, k)
print("Values of the k largest entries:", values.numpy())
print("Indices of the k largest entries:", indices.numpy())
