import tensorflow as tf

def fractional_avg_pooling(input_tensor, pooling_ratio):
    """Performs fractional average pooling on the input."""
    batch, height, width, channels = input_tensor.get_shape().as_list()

    new_height = int(height / pooling_ratio)
    new_width = int(width / pooling_ratio)

    # Create indices along spatial dimensions
    h_idx = tf.range(new_height)
    w_idx = tf.range(new_width)

    # Create a meshgrid along these indices
    h_offset, w_offset = tf.meshgrid(h_idx, w_idx)
    h_offset = tf.cast(h_offset, dtype=tf.float32)
    w_offset = tf.cast(w_offset, dtype=tf.float32)

    # Reshape them such that when flattened, each offset corresponds to a unique pooling region
    h_offset = tf.reshape(h_offset, [-1])
    w_offset = tf.reshape(w_offset, [-1])

    # Multiply them with the pooling ratio to get the top left corner of each pooling region
    h_start = h_offset * pooling_ratio
    w_start = w_offset * pooling_ratio

    # Create tensor elements to use for fractional pooling
    box_sizes = tf.fill([new_height * new_width], pooling_ratio)
    box_row_lengths = tf.fill([new_height * new_width], new_width)

    # Perform fractional average pooling using the TF's raw_ops function
    output = tf.raw_ops.AvgPool3DGrad(input_tensor,
                                      ksize=[1, 1, int(pooling_ratio**2)],
                                      strides=[1, 1, int(pooling_ratio**2)],
                                      padding='VALID',
                                      row_pooling_sequence=h_start,
                                      col_pooling_sequence=w_start,
                                      box_row_lengths=box_row_lengths,
                                      box_sizes=box_sizes)
    return output
