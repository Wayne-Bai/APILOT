import tensorflow as tf

def reverse_variable_length_slices(input_tensor, sizes):
    # Create a TensorFlow variable from the input tensor
    input_var = tf.Variable(input_tensor)

    # Use tf.gather to extract the slices in reverse order
    reversed_tensor = tf.ragged.boolean_mask(input_var, tf.range(tf.shape(input_var)[0])[:, None] < sizes)

    return reversed_tensor

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])
sizes = tf.constant([3, 2, 1, 0])

output = reverse_variable_length_slices(input_tensor, sizes)
print(output)
