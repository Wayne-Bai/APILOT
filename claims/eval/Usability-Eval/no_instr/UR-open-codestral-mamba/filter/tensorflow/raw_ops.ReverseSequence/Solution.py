import tensorflow as tf

def reverse_tensor_slices(tensor):
    # Create a reversed range tensor
    reversed_range = tf.reverse(tf.range(tf.shape(tensor)[0]), [True])

    # Gather tensor slices based on the reversed range and return
    return tf.gather(tensor, reversed_range)

input_tensor = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8]])
print(reverse_tensor_slices(input_tensor))
