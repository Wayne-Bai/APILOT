import tensorflow as tf

def fractional_max_pool_grad(orig_input, output, output_size, row_indices, col_indices):
    # Keeping the original tensor's properties
    orig_shape = tf.shape(orig_input)
    batch_size, orig_height, orig_width, channels = orig_shape[0], orig_shape[1], orig_shape[2], orig_shape[3]

    # Computing gradients for the Fractional Max Pool operation
    grad = tf.zeros_like(orig_input)

    for i in range(output_size[0]):
        for j in range(output_size[1]):
            row_index = row_indices[i, j]
            col_index = col_indices[i, j]

            # Accumulate gradients in the original input based on the output tensor
            grad[i, row_index, col_index, :] += output[i, j, :, :]

    return grad
