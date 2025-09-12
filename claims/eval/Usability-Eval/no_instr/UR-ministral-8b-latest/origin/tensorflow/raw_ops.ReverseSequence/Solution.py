import tensorflow as tf

# Define a function to reverse variable length slices using tf.slice
def reverse_slices(inputs, starts, ends):
    reversed_inputs = []
    for start, end in zip(starts, ends):
        reversed_slice = tf.raw_ops.Reverse(inputs=inputs[start:end],
                                           reverse_axis=0)
        reversed_inputs.append(reversed_slice)
    return tf.concat(reversed_inputs, axis=0)

# Example usage
input_tensor = tf.constant([1, 2, 3, 4, 5, 6])
starts = [0, 2]
ends = [3, 5]

# Call the function
output = reverse_slices(input_tensor, starts, ends)

# Print the output tensor
print(output.numpy())
