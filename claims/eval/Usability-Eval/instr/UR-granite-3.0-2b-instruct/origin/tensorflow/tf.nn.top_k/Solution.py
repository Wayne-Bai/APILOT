import tensorflow as tf

def find_k_largest(tensor, k):
    # Flatten the tensor along the last dimension
    flat_tensor = tf.reshape(tensor, (-1, tensor.shape[-1]))

    # Find the k largest values and their indices
    _, indices = tf.nn.top_k(flat_tensor, k)

    # Reshape the indices back to the original shape
    indices = tf.reshape(indices, tensor.shape[:-1] + [k])

    return flat_tensor[:k], indices

# Example usage:
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 3

values, indices = find_k_largest(tensor, k)

print("Values:")
print(values.numpy())
print("\nIndices:")
print(indices.numpy())
