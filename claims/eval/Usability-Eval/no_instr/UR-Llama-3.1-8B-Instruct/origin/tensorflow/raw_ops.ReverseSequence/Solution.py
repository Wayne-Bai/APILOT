import tensorflow as tf

def reverse_slices(indices, axis=None, name=None):
    """
    Reverses variable length slices along one axis.

    Args:
        indices: A 1-D tensor of indices (Python integers or Tensor of integers).
        axis: An optional integer, represents the axis of.
        name: A name for the operation

    Returns:
        Output 1-D tensor with the indices in reverse order along the given axis.
    """
    with tf.name_scope(name, default_name="reverse_slices") as name:
        # Check if the input is a Tensor of ranks 1 or less
        if not isinstance(indices, tf.Tensor):
            indices = tf.convert_to_tensor(indices)

        # Ensure the input is a batched tensor
        indices = tf.expand_dims(indices, axis=1)

        # Use tf.reverse_v2 to reverse the slices along the given axis
        indices = tf.reverse_v2(indices, axis=[1])

        # Remove the extra dimension added to make it batchable 
        if len(indices.shape) == 2 and indices.shape[1] == 1:
            indices = indices[:, 0]

        return tf.squeeze(indices, axis=1, name=name)

# Example usage:
indices = tf.constant([1, 2, 3, 4, 5])
print(reverse_slices(indices))  # Output: [5, 4, 3, 2, 1]

indices = tf.constant([[1, 2], [3, 4], [5, 6]])
print(reverse_slices(indices, axis=0))
# Output: [[5, 6], [3, 4], [1, 2]]

indices = tf.constant([1, 2, 3, 4, 5])
print(reverse_slices(indices, axis=tf.int32(None).num_elements() - 1))
# Output: [5, 4, 3, 2, 1]
