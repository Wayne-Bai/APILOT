import tensorflow as tf

def top_k_values_and_indices(tensor, k):
    # Get the shape of the tensor
    shape = tf.shape(tensor)

    # Validate input
    if k > shape[-1]:
        raise ValueError(f"k cannot be greater than the size of the last dimension, which is {shape[-1]}.")

    # Get the last dimension
    last_dim = tensor

    # Compute the k largest values along the last dimension
    sorted_values, _ = tf.nn.top_k(last_dim, k=k, sorted=True)

    # Get the indices of the k largest values
    sorted_indices = tf.range(shape[-1], dtype=tf.int32)[:k][tf.argsort(last_dim, direction='DESCENDING')[:k]]

    return sorted_values, sorted_indices

# Example usage
tensor = tf.constant([[3, 7, 2], [1, 5, 0], [9, 2, 2]])
k = 2

sorted_values, sorted_indices = top_k_values_and_indices(tensor, k)

print("Sorted Values:")
print(sorted_values.numpy())
print("\nSorted Indices:")
print(sorted_indices.numpy())
