import tensorflow as tf

def fill_empty_rows(input_tensor, default_value):
    # Get the shape of the input tensor
    shape = input_tensor.shape

    # Get the indices and values of the non-empty rows
    indices = tf.where(tf.reduce_sum(input_tensor.values, axis=1) > 0)
    values = tf.gather_nd(input_tensor.values, indices)

    # Create a new tensor with the same shape as the input tensor
    output_tensor = tf.SparseTensor(tf.zeros([shape[0], 1], dtype=tf.int64),
                                    tf.fill([shape[0], 1], default_value),
                                    shape)

    # Set the values of the non-empty rows in the output tensor
    output_tensor = tf.scatter_nd(indices, values, output_tensor.shape)

    return output_tensor
