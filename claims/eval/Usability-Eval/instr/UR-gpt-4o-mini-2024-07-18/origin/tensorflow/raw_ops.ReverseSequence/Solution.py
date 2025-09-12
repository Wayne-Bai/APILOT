import tensorflow as tf

def reverse_variable_length_slices(input_tensor, lengths):
    # Create a Tensor array from the input tensor and lengths
    reversed_slices = tf.TensorArray(dtype=input_tensor.dtype, size=tf.shape(lengths)[0])
    
    def reverse_slice(i):
        # Get the starting index for each slice
        start_idx = tf.reduce_sum(lengths[:i])
        # Get the length of the current slice
        current_length = lengths[i]
        # Extract and reverse the slice
        return tf.reverse(input_tensor[start_idx:start_idx + current_length], axis=[0])

    # Populate the TensorArray with reversed slices
    for i in tf.range(tf.shape(lengths)[0]):
        reversed_slice = reverse_slice(i)
        reversed_slices = reversed_slices.write(i, reversed_slice)

    # Stack the slices back into a tensor
    result = reversed_slices.stack()
    return result

# Example usage
input_tensor = tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.int32)
lengths = tf.constant([2, 2, 2], dtype=tf.int32)
reversed_result = reverse_variable_length_slices(input_tensor, lengths)

tf.print(reversed_result)  # Outputs the reversed slices
