import tensorflow as tf

def reverse_slices(input_tensor, begin, end):
    """
    Reverses variable length slices of the elements along the
    given dimension in the input tensor.

    Args:
        input_tensor: The input tensor.
        begin: The start of the input tensor, sliced along the given dimension.
            It is similar to tf.slice's begin parameter. It is an int32 vector,
            representing the index to start each slice.
        end: The end of the input tensor, sliced along the given dimension.
            It is similar to tf.slice's size parameter. It is an int32 vector,
            representing the size of each slice.

    Returns:
        The reversed variable length slices.
    """
    # Split the input tensor into slices
    sliced_tensor = tf.raw_ops.Split(input=input_tensor, num_split=end)

    # Reverse each slice and stack them back together
    reversed_slices = tf.raw_ops.ReverseV2(input=sliced_tensor, axis=-1)

    # Stack the reversed slices back together
    result = tf.raw_ops.ConcatV2(input=tf.nest.flatten(reversed_slices), axis=0, name='reversed_scores_concat')

    return result

# Create a sample tensor with shape (2, 4, 3)
input_tensor = tf.constant([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]
])

# Define the begin and end indices
begin = tf.constant([0, 0, 0])
end = tf.constant([3, 2, 5])

# Use the custom function to reverse the slices
output = reverse_slices(input_tensor, begin, end)

with tf.Session() as sess:
    print(sess.run(output))
